import os
import shutil
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import time
import datetime
import zipfile
import random


# TEXT FUNCTIONS

class MyHTMLParser(HTMLParser):
    pcount = 0
    captchure = False
    title = ""

    def handle_starttag(self, tag, attrs):
        if tag == "p" and self.pcount == 0:
            self.captchure = True

        self.pcount += self.pcount + 1

    def handle_data(self, data):
        if self.captchure and self.pcount == 1:
            self.captchure = False
            self.title = data


def getttile(file):
    with open(file, mode="r", encoding="utf-8") as f:
        html = f.read()
        parser = MyHTMLParser()
        parser.feed(html)
        return parser.title


today = str(date.today())



# HEADER AND FOOTER

footerfile = "./files/python-footer.html"
headerfile = "./files/python-header.html"


footerhtml = ""
headerhtml = ""

with open(headerfile, mode="r", encoding="utf-8") as f:
    headerhtml = f.read()

with open(footerfile, mode="r", encoding="utf-8") as f:
    footerhtml = f.read()

footerhtml = footerhtml.replace("#date#", today)


  
# CODES 

projects = [
    {"name": "roach-race", "files": [], "url": "/race/"},
    {"name": "xmla", "files": [], "url": "/catalog/"},
    {"name": "lottery-salt-emulator", "files": [], "url": "/all/"}
]


codesdir = "./python//static/imgs/"
projectsdir = "../projects/"

contentfrontproj = {}

for p in projects: 
    with open(str(projectsdir) + "/" + p["name"] + "/README.md", mode="r", encoding="utf-8") as f:  
        lines = list(f)
        strlines = lines[1:len(lines)]            
        contentstr = "".join(strlines)
        contentfrontproj[p["name"]] = "<h2>" + lines[0] + "</h2>" + contentstr.replace("  ", "</br>")  + "</br></br>"
    for f in p["files"]:
        file = codesdir + "/" + p["name"] + "/" + f       
        os.makedirs(os.path.dirname(file), exist_ok=True)
        oldfile = str(projectsdir) + "/" + p["name"] + "/" + f
        print("copied " + p["name"] + " " + f)
        shutil.copyfile(oldfile, file)
    oldimgfile = str(projectsdir) + "/" + p["name"] + "/" + p["name"] + ".jpg"
    newimgfile = codesdir + p["name"] + ".jpg"
    shutil.copyfile(oldimgfile, newimgfile)
    print("copied " + oldimgfile)

beginhtml = '''<div class="text-codes"><p class="content-text__title">
            Тестовые проекты Python:
        </p>'''
endhtml = '''
        </div>'''

htmlcodes = "<ul class='clilist'>" 
for p in projects: 
    file = p["name"] 
    if not os.path.isfile(file):
        htmlcodes += "<p>" + contentfrontproj[file] 
        imgpath = "/static/imgs/" + file + ".jpg"
        htmlcodes += "<a href='" + imgpath + "'><img width='300px' src='" + imgpath +"'/></a>"
        htmlcodes += "<li>" + "<a class='link' href='https://gitflic.ru/project/evgeniyvinokurov/" + file + "/'>gitflic</a>"
        if len(p["files"]) > 0:
            htmlcodes += "&nbsp;&nbsp;<a class='link' href='/" + file + "/'>demo</a>"
        if "url" in p:
            htmlcodes += "&nbsp;&nbsp;<a class='link' href='" + p["url"] + "'>demo</a>"        
        htmlcodes += "</li>" + "</p>"
        htmlcodes += "<br/><br/><br/>"
htmlcodes += "</ul>"

preimgindexfile = "./python/views/index-python.html"
os.makedirs(os.path.dirname(preimgindexfile), exist_ok=True)
indexpreimghtml =  headerhtml + beginhtml + htmlcodes + endhtml + footerhtml


with open(preimgindexfile, mode="w", encoding="utf-8") as f:
    f.write(indexpreimghtml) 
    print("written: " + preimgindexfile)

precssfile = "./python/static/css/main.css"
os.makedirs(os.path.dirname(precssfile), exist_ok=True)
shutil.copyfile("./css/main.css", precssfile)
print("css copied")

