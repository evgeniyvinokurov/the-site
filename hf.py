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

refaqfilemain = "./index.html" 
beginhtml = "<div class='faq'>"
endhtml = "</div>"
faqfilemainhtml =  headerhtml + beginhtml + faqhtml + endhtml + footerhtml
    
os.makedirs(os.path.dirname(refaqfilemain), exist_ok=True)
with open(refaqfilemain, mode="w", encoding="utf-8") as f:
    f.write(faqfilemainhtml) 
    print("written: " + refaqfilemain)

ti_m = os.path.getmtime(faqfilemain)
tdate = datetime.datetime.utcfromtimestamp(ti_m).strftime('%Y-%m-%d')    


# TEXTS
    
dirtexts = "./files/texts/"
textsfilemain = "./files/texts/index.html"
dirparsed = "./texts/"
textshtml = ""

with open(textsfilemain, mode="r", encoding="utf-8") as f:
    textshtml = f.read()
    
htmlcontentindextexts = "" 
for file in os.listdir(dirtexts):
    indexfile = file + "/index.html"
    if os.path.isfile(dirtexts + indexfile):
        html = ""
        refile = dirparsed + indexfile
        with open(dirtexts + indexfile, mode="r", encoding="utf-8") as f:
            html = f.read()

        ti_m = os.path.getmtime(dirtexts + indexfile)
        tdate = datetime.datetime.utcfromtimestamp(ti_m).strftime('%Y-%m-%d')        

        bhtml = "<div class='clilist'>"
        ehtml = "</div>"

        refilehtml = headerhtml + bhtml + html + ehtml + footerhtml
        os.makedirs(os.path.dirname(refile), exist_ok=True)
        with open(refile, mode="w", encoding="utf-8") as f:
            f.write(refilehtml) 
            link = "<li ><span>" + getttile(dirtexts + indexfile) + "</span> <a class='link' href='" + indexfile  + "'>-></a></li>"
            
            htmlcontentindextexts = htmlcontentindextexts + link
            print("written: " + refile)

beginhtml = '''<p class="content-text__title">
            Тексты:
        </p>
        <ul class="text-texts list">'''
endhtml = '''
        </ul>'''
htmlcontent = textshtml + beginhtml + htmlcontentindextexts + endhtml


indexfiletexts = dirparsed + "index.html" 
indexfiletextshtml = headerhtml + htmlcontent + footerhtml
with open(indexfiletexts, mode="w", encoding="utf-8") as f:
    f.write(indexfiletextshtml) 
    print("written: " + indexfiletexts)



  
# CODES 

projects = [
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
    {"name": "e-shop-client", "files": [
        "/assets/img/1484.gif",
        "/assets/img/favicon.png",
        "/assets/style.css",
        "bundle.js",
        "index.html"
    ]},
    {"name": "bus-tickets", "files": [
        "/css/style.css",
        "/imgs/down.png",
        "/imgs/pattern.png",
        "all.js",
        "index.html"
    ]},
    {"name": "roach-race", "files": []},
    {"name": "get-your-song", "files": []},
    {"name": "xmla", "files": []},
    {"name": "deezer-api-albums-php", "files": []}
]
random.shuffle(projects)

codesdir = "./codes/"
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
            Коды:
        </p>'''
endhtml = '''
        </div>'''

codesdir = "./codes/"
htmlcodes = "<ul class='clilist'>" 
for p in projects: 
    file = p["name"] 
    if not os.path.isfile(file):
        htmlcodes += "<p>" + contentfrontproj[file] 
        imgpath = "/" + file + ".jpg"
        htmlcodes += "<a href='/codes/" + imgpath + "'><img width='300px' src='/codes/" + imgpath +"'/></a>"
        htmlcodes += "<li>" + "<a class='link' href='https://gitflic.ru/project/evgeniyvinokurov/" + file + "/'>gitflic</a>"
        if len(p["files"]) > 0:
            htmlcodes += "&nbsp;&nbsp;<a class='link' href='/codes/" + file + "/'>demo</a>"
        htmlcodes += "</li>" + "</p>"
        htmlcodes += "<br/><br/><br/>"
htmlcodes += "</ul>"

preimgindexfile = "./codes/index.html"
os.makedirs(os.path.dirname(preimgindexfile), exist_ok=True)
indexpreimghtml =  headerhtml + beginhtml + htmlcodes + endhtml + footerhtml


with open(preimgindexfile, mode="w", encoding="utf-8") as f:
    f.write(indexpreimghtml) 
    print("written: " + preimgindexfile)



