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

def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

def getttile(file):
    with open(file, mode="r", encoding="utf-8") as f:
        html = f.read()
        parser = MyHTMLParser()
        parser.feed(html)
        return parser.title


today = str(date.today())



# HEADER AND FOOTER

footerfile = "./files/footer.html"
headerfile = "./files/header.html"


footerhtml = ""
headerhtml = ""

with open(headerfile, mode="r", encoding="utf-8") as f:
    headerhtml = f.read()

with open(footerfile, mode="r", encoding="utf-8") as f:
    footerhtml = f.read()

footerhtml = footerhtml.replace("#date#", today)



# FAQ INDEX
    
faqfilemain = "./files/faq/index.html"
faqhtml = ""

with open(faqfilemain, mode="r", encoding="utf-8") as f:
    faqhtml = f.read()

refaqfilemain = "./common/faq/index.html" 
beginhtml = "<div class='faq'>"
endhtml = "</div>"
faqfilemainhtml =  headerhtml + beginhtml + faqhtml + endhtml + footerhtml
    
os.makedirs(os.path.dirname(refaqfilemain), exist_ok=True)
with open(refaqfilemain, mode="w", encoding="utf-8") as f:
    f.write(faqfilemainhtml) 
    print("written: " + refaqfilemain)

ti_m = os.path.getmtime(faqfilemain)
tdate = datetime.datetime.utcfromtimestamp(ti_m).strftime('%Y-%m-%d')    


  
# CODES 

projects = [
    {"name": "bus-tickets", "tags": ["js", "markup", "gulp"], "dirs": ["imgs", "css"],  "files": [
        "all.js",
        "index.html"
    ]},
    {"name": "e-shop-client", "tags": ["js", "markup", "webpack", "catalog", "cart", "vuejs", "canvas", "sass"], "dirs": ["assets"], "files": [
        "bundle.js",
        "index.html"
    ]},
    {"name": "dances", "tags": ["js", "markup", "ymaps", "svg", "gulp", "jquery", "sass"], "dirs": [
        "Bongos",
        "css",
        "fonts",
        "imgs"
        ], "files": [
        "all.js",        
        "index.html"]
    },
    {"name": "jsons-arrays", "tags": ["json", "js"], "files": [
        "/css/main.css",
        "all.js",
        "index.html"
    ]},
    {"name": "quest-thing", "tags": ["json", "js", "jquery"], "dirs": ["css"], "files": [
        "all.js",
        "index.html",
        "index-constructor.html"
    ]},
    {"name": "text-animation","tags": ["jquery", "js", "markup"], "dirs": ["css"], "files": [
        "all.js",
        "index.html"
    ]},
    {"name": "basic-tetris","tags": ["js", "canvas"], "files": [
        "tetris.js",
        "index.html"
    ]},
    {"name": "users","tags": ["js", "angular", "material", "typescript", "markup", "sass"], "dirs": ["app"], "files": [], "baseUrl": "app/"},
    {"name": "deezer-api-albums-php", "tags": ["php", "sqlite", "api", "deezer", "sql"], "files": [], "url": "http://www.evgeniyvinokurov.byethost9.com/albums/"},
    {"name": "get-your-song", "tags": ["php", "eightball"], "files": [], "url": "http://www.evgeniyvinokurov.byethost9.com/get-your-song/"},
    {"name": "api-calls", "tags": ["php", "api"], "files": [], "url": "http://www.evgeniyvinokurov.byethost9.com/api-calls/"},
    {"name": "roach-race", "tags": ["python", "vanillajs", "xml", "bottle"], "files": [], "url": "http://evgeniyvinokurov.pythonanywhere.com/race/"},
    {"name": "xmla", "tags": ["python", "vanillajs", "xml", "bottle", "catalog", "cart", "markup", "pytest", "selenium", "docker"], "files": [], "url": "http://evgeniyvinokurov.pythonanywhere.com/catalog/"},
    {"name": "veggy-farm", "tags": ["python", "gulp", "webpack", "django", "catalog", "markup", "docker", "sqlite", "sass", "jquery", "vuejs"], "files": []},
    {"name": "python-scripts", "video": "true", "tags": ["python", "eightball", "ffmpeg", "moviepy", "mp4"], "files": []},
    {"name": "story-linker", "tags": ["python", "fastapi", "pika", "vanillajs"], "files": []},
    {"name": "lottery-salt-emulator", "tags": ["python", "bottle", "xml", "vanillajs", "eightball"], "files": [], "url": "http://evgeniyvinokurov.pythonanywhere.com/all/"},
    {"name": "base-python-app-for-web", "tags": ["python", "bottle", "xml", "vuejs", "markup"], "files": [], "url": "http://evgeniyvinokurov.pythonanywhere.com/feedback/"}
];


codesdir = "./common/demo/"
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
    if "dirs" in p:
        for d in p["dirs"]:
            dir = codesdir + "/" + p["name"] + "/" + d
            copy_and_overwrite(str(projectsdir) + "/" + p["name"] + "/" + d, dir)
    if "video" not in p:    
        oldimgfile = str(projectsdir) + "/" + p["name"] + "/" + p["name"] + ".jpg"
        newimgfile = codesdir + p["name"] + ".jpg"
        shutil.copyfile(oldimgfile, newimgfile)
        print("copied " + oldimgfile)
    else:        
        oldvidfile = str(projectsdir) + "/" + p["name"] + "/" + p["name"] + ".mp4"
        newimgfile = codesdir + p["name"] + ".mp4"
        shutil.copyfile(oldvidfile, newimgfile)
        print("copied " + oldvidfile)

beginhtml = '''<div class="text-codes"><p class="content-text__title">
        </p>'''
endhtml = '''
        </div>'''

codesdir = "./demo/"
htmlcodes = "<ul class='clilist'>" 
for p in projects: 
    file = p["name"] 
    if not os.path.isfile(file):
        htmlcodes += "<div class='project " + " ".join(p["tags"]) + "'><p>" + contentfrontproj[file] 
        if "video" not in p:
            imgpath = "/demo/" + file + ".jpg"
            htmlcodes += "<a href='" + imgpath + "'><img width='300px' src='" + imgpath +"'/></a>"
        else:
            videosrc = "/demo/" + file + ".mp4"
            htmlcodes += "<video controls width='250'><source src='" + videosrc + "' type='video/mp4' /></video>"
        htmlcodes += "<li>" + "<a class='link' href='https://gitflic.ru/project/evgeniyvinokurov/" + file + "/'>gitflic</a>"
        if len(p["files"]) > 0 or "dirs" in p:
            htmlcodes += "&nbsp;&nbsp;<a class='link' href='/demo/" + file + "/" + (p["baseUrl"] if "baseUrl" in p else "") + "'>demo</a>"
        if "url" in p:
            htmlcodes += "&nbsp;&nbsp;<a class='link' href='" + p["url"] + "'>demo</a>"        
        htmlcodes += "</li>" + "</p></div>"
htmlcodes += "</ul>"

preimgindexfile = "./common/index.html"
os.makedirs(os.path.dirname(preimgindexfile), exist_ok=True)
indexpreimghtml =  headerhtml + beginhtml + htmlcodes + endhtml + footerhtml


with open(preimgindexfile, mode="w", encoding="utf-8") as f:
    f.write(indexpreimghtml) 
    print("written: " + preimgindexfile)


precssfile = "./common/css/main.css"
os.makedirs(os.path.dirname(precssfile), exist_ok=True)
shutil.copyfile("./css/main.css", precssfile)
print("css copied")

