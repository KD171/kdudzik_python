#! /usr/bin/env python3
import os
import json


class JsonEditor:

    def __init__(self):
        self.clear()
        self.file_name = "db.json"
        self.data = None
        self.startup()
        self.chose()

    def startup(self):
        if not os.path.isfile(self.file_name):
            file = open("db.json", 'w+')
            self.data = {"movies": []}
            self.updateFile()
            file.close()
        self.readFromJson()
        self.printJson()

    def updateFile(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f, indent=3)

    def readFromJson(self):
        with open(self.file_name) as json_file:
            self.data = json.load(json_file)

    def addElementToJson(self):
        print("Add new element to DB")
        data = {
            "title": input("Movie Title: "),
            "year": input("Year: "),
            "type": input("Type: ")
        }
        self.data["movies"].append(data)
        self.updateFile()

    def delElementFromJson(self):
        movie = input("Type movie title to delete from db: ")
        movieInDB = len(self.data['movies'])
        for x in self.data["movies"]:
            if x["title"] == movie:
                self.data["movies"].remove(x)
                self.updateFile()
        if len(self.data['movies']) == movieInDB:
            print("Can't find movie \"%s\" in JSON" % movie)
        else:
            print("Movie \"%s\" is delete from JSON" % movie)

    def clear(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def printJson(self):
        try:
            if len(self.data["movies"]) > 0:
                print("%-30s %-10s %-30s" % ("Title", "Year", "Type"))
                for movie in self.data["movies"]:
                    print("%-30s %-10s %-30s" % (movie["title"], movie["year"], movie["type"]))
        except Exception as e:
            os.remove(self.file_name)
            print("json file is broken, rerun script and try again")

    def chose(self):
        chose = input("Add data [insert: a]\nDelete data [insert: d]\nExit [type: exit]\n")
        if chose == "a":
            self.clear()
            self.addElementToJson()
        elif chose == "d":
            self.clear()
            self.delElementFromJson()
        elif chose == "exit":
            exit()
        else:
            print("Try again")


if __name__ == '__main__':
    JsonEditor()
