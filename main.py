import xml.etree.ElementTree as ET
import xml

data = {}


def parseXML(xmlitem):
    data[xmlitem.tag] = []
    if type(xmlitem) == xml.etree.ElementTree.Element:
        for item in xmlitem:
            data[xmlitem.tag].append(parseXML(item))
    else:
        return xmlitem.tag
    # return news items list


if __name__ == "__main__":
    tree = ET.parse("text.xml")

    root = tree.getroot()

    parseXML(root)
    print(data)
