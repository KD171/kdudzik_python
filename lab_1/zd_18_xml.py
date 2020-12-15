#! /usr/bin/env python3
from xml.dom import minidom
import xml.sax

file = "xmlFile.xml"
newFile = "newXmlFile.xml"


def DomEditXML():
    dom = minidom.parse("xmlFile.xml")
    movieTitle = dom.getElementsByTagName("title")[0].getAttribute("title")
    yearOld = dom.getElementsByTagName("title")[0].getElementsByTagName("year")[0].firstChild.data
    dom.getElementsByTagName("title")[0].setAttribute("title", "The Godfather 2")
    dom.getElementsByTagName("title")[0].getElementsByTagName("year")[0].firstChild.data = 1980
    movieTitleNew = dom.getElementsByTagName("title")[0].getAttribute("title")
    yearNew = dom.getElementsByTagName("title")[0].getElementsByTagName("year")[0].firstChild.data
    file = open(newFile, "w+")
    dom.writexml(file)
    file.close()
    print("---------------------------- DOM Edit XML ----------------------------")
    print("Old value of the year attribute: %s for the movie \"%s\"" % (yearOld, movieTitle))
    print("New value of the year attribute: %s for the movie \"%s\"" % (yearNew, movieTitleNew))
    print("File: ", file.name)
    print("")


class SaxHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.Element = ''
        self.title = ''
        self.year = ''
        self.genre = ''

    def startElement(self, tag, attributes):
        self.Element = tag
        if tag == "title":
            print("Movie details:")
            self.title = attributes["title"]
            print("\tTitle:", self.title)

    def endElement(self, tag):
        if self.Element == "year":
            print("\tYear:", self.year)
        elif self.Element == "genre":
            print("\tGenre:", self.genre)
        self.Element = ""

    def characters(self, content):
        if self.Element == "title":
            self.title = content
        elif self.Element == "year":
            self.year = content
        elif self.Element == "genre":
            self.genre = content


def SaxRaedXML(filename):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(SaxHandler())
    parser.parse(filename)


SaxRaedXML(file)
DomEditXML()
SaxRaedXML(newFile)
