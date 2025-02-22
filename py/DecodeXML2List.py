# 读取xml文件（其实是.anm2文件），获取动画的信息
from tokenize import Double
from xml.dom.minidom import parse
import xml.dom.minidom

def DecodeXML(file):
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(file)
    # 获取文档唯一根节点
    DOMTreeRoot = DOMTree.documentElement
    return DOMTreeRoot

def GetAnimationInfo(DOMTreeRoot):
    AnimationInfo = {}
    XML_InfoList = DOMTreeRoot.getElementsByTagName("Info")
    for XML_Info in XML_InfoList:
        AnimationInfo["Fps"] = XML_Info.getAttribute("Fps")
        AnimationInfo["Version"] = XML_Info.getAttribute("Version")
    ##
    XML_SpritesheetList = DOMTreeRoot.getElementsByTagName("Spritesheet")
    SpritesheetDir = {}
    for XML_Spritesheet in XML_SpritesheetList:
        SpritesheetDir[XML_Spritesheet.getAttribute("Id")] = XML_Spritesheet.getAttribute("Path")
    # print(SpritesheetDir)
    ##
    XML_LayerList = DOMTreeRoot.getElementsByTagName("Layer")
    AnimationInfo["LayerInfo"] = []
    for XML_Layer in XML_LayerList:
        LayerInfoDir = {}
        LayerInfoDir["Id"] = XML_Layer.getAttribute("Id")
        LayerInfoDir["Name"] = XML_Layer.getAttribute("Name")
        LayerInfoDir["Path"] = SpritesheetDir[XML_Layer.getAttribute("SpritesheetId")]
        AnimationInfo["LayerInfo"].append(LayerInfoDir)
    # print(AnimationInfo)
    return AnimationInfo

def GetAnimationFrame(DOMTreeRoot):
    AnimaitionList =  []
    XML_AnimationList = DOMTreeRoot.getElementsByTagName("Animation")
    for XML_Animation in XML_AnimationList:
        AnimationDir = {}
        AnimationDir["Name"] = XML_Animation.getAttribute("Name")
        AnimationDir["FrameNum"] = int(XML_Animation.getAttribute("FrameNum"))
        AnimationDir["LayerAnimationList"] = []
        XML_LayerAnimationList = XML_Animation.getElementsByTagName("LayerAnimation")
        for XML_LayerAnimation in XML_LayerAnimationList:
            LayerAnimationDir = {}
            LayerAnimationDir["LayerId"] = XML_LayerAnimation.getAttribute("LayerId")
            LayerAnimationDir["Visible"] = XML_LayerAnimation.getAttribute("Visible")
            LayerAnimationDir["FrameList"] = []
            XML_FrameList = XML_LayerAnimation.getElementsByTagName("Frame")
            for XML_Frame in XML_FrameList:
                FrameDir = {}
                FrameDir['XPosition'] = float(XML_Frame.getAttribute('XPosition'))
                FrameDir['YPosition'] = float(XML_Frame.getAttribute('YPosition'))
                FrameDir['XPivot'] = float(XML_Frame.getAttribute('XPivot'))
                FrameDir['YPivot'] = float(XML_Frame.getAttribute('YPivot'))
                FrameDir['XCrop'] = float(XML_Frame.getAttribute('XCrop'))
                FrameDir['YCrop'] = float(XML_Frame.getAttribute('YCrop'))
                FrameDir['Width'] = float(XML_Frame.getAttribute('Width'))
                FrameDir['Height'] = float(XML_Frame.getAttribute('Height'))
                FrameDir['XScale'] = float(XML_Frame.getAttribute('XScale'))
                FrameDir['YScale'] = float(XML_Frame.getAttribute('YScale'))
                FrameDir['Delay'] = int(XML_Frame.getAttribute('Delay'))
                FrameDir['Visible'] = XML_Frame.getAttribute('Visible')
                FrameDir['RedTint'] = float(XML_Frame.getAttribute('RedTint'))
                FrameDir['GreenTint'] = float(XML_Frame.getAttribute('GreenTint'))
                FrameDir['BlueTint'] = float(XML_Frame.getAttribute('BlueTint'))
                FrameDir['AlphaTint'] = float(XML_Frame.getAttribute('AlphaTint'))
                FrameDir['RedOffset'] = float(XML_Frame.getAttribute('RedOffset'))
                FrameDir['GreenOffset'] = float(XML_Frame.getAttribute('GreenOffset'))
                FrameDir['BlueOffset'] = float(XML_Frame.getAttribute('BlueOffset'))
                FrameDir['Rotation'] = float(XML_Frame.getAttribute('Rotation'))
                FrameDir['Interpolated'] = XML_Frame.getAttribute('Interpolated')
                LayerAnimationDir["FrameList"].append(FrameDir)
            AnimationDir["LayerAnimationList"].append(LayerAnimationDir)
        AnimaitionList.append(AnimationDir)
    return AnimaitionList
    
