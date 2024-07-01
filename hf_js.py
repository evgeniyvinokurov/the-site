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

footerfile = "./files/js-footer.html"
headerfile = "./files/js-header.html"


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

refaqfilemain = "./js/faq/index.html" 
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
    {"name": "bus-tickets", "files": [
        "/css/style.css",
        "/imgs/down.png",
        "/imgs/pattern.png",
        "all.js",
        "index.html"
    ]},
    {"name": "e-shop-client", "files": [
        "/assets/style.css",
        "/assets/img/1484.gif",
        "/assets/img/favicon.png",
        "bundle.js",
        "index.html"
    ]},
    {"name": "dances", "files": [
        "all.js",
        "/Bongos/hihat.wav",
        "/Bongos/kick2.wav",
        "/Bongos/kick.wav",
        "/Bongos/snare.wav",
        "/Bongos/tom12.wav",
        "/Bongos/tom1.wav",
        "/Bongos/tom2.wav",
        "/Bongos/tom3.wav",
        "/css/main.css",
        "/fonts/basic/font-webfont.ttf",
        "/fonts/basic/font-webfont.woff",
        "/fonts/basic/font-webfont.woff2",
        "/imgs/button1.png",
        "/imgs/button2.png",
        "/imgs/button3.png",
        "/imgs/button4.png",
        "/imgs/button5.png",
        "/imgs/button6.png",
        "/imgs/calendar.png",
        "/imgs/checklist.png",
        "/imgs/facebook.png",
        "/imgs/footer_logo.png",
        "/imgs/header_logo.png",
        "/imgs/info_cats_2.png",
        "/imgs/info_cats.png",
        "/imgs/info.png",
        "/imgs/phone.png",
        "/imgs/pinterest.png",
        "/imgs/placemark.png",
        "/imgs/rss.png",
        "/imgs/search.png",
        "/imgs/share.png",
        "/imgs/slider_cats_2.png",
        "/imgs/slider_cats_3.png",
        "/imgs/slider_cats.png",
        "/imgs/tam1.png",
        "/imgs/tam2.png",
        "/imgs/tam3.png",
        "/imgs/tam4.png",
        "/imgs/tam5.png",
        "/imgs/tam6.png",
        "/imgs/tam7.png",
        "/imgs/tam8.png",
        "/imgs/totheleft.png",
        "/imgs/totheright.png",
        "/imgs/translation.png",
        "/imgs/twitter.png",
        "/imgs/ufo2.png",
        "/imgs/ufocats.png",
        "/imgs/ufo.png",
        "/imgs/ukulele.png",
        "/imgs/warning.png",
        "index.html"]
    },
    {"name": "jsons-arrays", "files": [
        "/css/main.css",
        "all.js",
        "index.html"
    ]},
    {"name": "quest-thing", "files": [
        "/css/main.css",
        "/css/treejs/32px.png",
        "/css/treejs/throbber.gif",
        "/css/treejs/40px.png",
        "/css/treejs/style.min.css",
        "all.js",
        "index.html",
        "index-constructor.html"
    ]},
    {"name": "text-animation", "files": [
        "/css/main.css",
        "all.js",
        "index.html"
    ]},
    {"name": "basic-tetris", "files": [
        "tetris.js",
        "index.html"
    ]},{"name": "users", "files": [
        "/app/assets/MOCK_DATA.json",
        "/app/favicon.ico",
        "/app/index.html",
        "/app/main-3JO4DNX4.js",
        "/app/polyfills-6EAL64PA.js",
        "/app/styles-BJXQGC3E.css",
    ], "baseUrl": "app/"},
    {"name": "base-python-app-for-web", "files": [], "url": "evgeniyvinokurov.pythonanywhere.com/feedback/"}
];


codesdir = "./js/demo/"
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
            Тестовые проекты JS:
        </p>'''
endhtml = '''
        </div>'''

codesdir = "./demo/"
htmlcodes = "<ul class='clilist'>" 
for p in projects: 
    file = p["name"] 
    if not os.path.isfile(file):
        htmlcodes += "<p>" + contentfrontproj[file] 
        imgpath = "/demo/" + file + ".jpg"
        htmlcodes += "<a href='" + imgpath + "'><img width='300px' src='" + imgpath +"'/></a>"
        htmlcodes += "<li>" + "<a class='link' href='https://gitflic.ru/project/evgeniyvinokurov/" + file + "/'>gitflic</a>"
        if len(p["files"]) > 0:
            htmlcodes += "&nbsp;&nbsp;<a class='link' href='/demo/" + file + "/" + (p["baseUrl"] if "baseUrl" in p else "") + "'>demo</a>"
        if "url" in p:
            htmlcodes += "&nbsp;&nbsp;<a class='link' href='" + p["url"] + "'>demo</a>"        
        htmlcodes += "</li>" + "</p>"
        htmlcodes += "<br/><br/><br/>"
htmlcodes += "</ul>"

preimgindexfile = "./js/index.html"
os.makedirs(os.path.dirname(preimgindexfile), exist_ok=True)
indexpreimghtml =  headerhtml + beginhtml + htmlcodes + endhtml + footerhtml


with open(preimgindexfile, mode="w", encoding="utf-8") as f:
    f.write(indexpreimghtml) 
    print("written: " + preimgindexfile)


precssfile = "./js/css/main.css"
os.makedirs(os.path.dirname(precssfile), exist_ok=True)
shutil.copyfile("./css/main.css", precssfile)
print("css copied")

