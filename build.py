import os
import shutil
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import time
import datetime
import zipfile
import random
import json


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

footerfile = "./sources/footer.html"
headerfile = "./sources/header.html"
morefile = "./sources/more.html"
indexfile = "./sources/index.html"


footerhtml = ""
headerhtml = ""
morefilehtml = ""
indexfilehtml = ""

with open(headerfile, mode="r", encoding="utf-8") as f:
    headerhtml = f.read()

with open(footerfile, mode="r", encoding="utf-8") as f:
    footerhtml = f.read()

with open(morefile, mode="r", encoding="utf-8") as f:
    morefilehtml = f.read()

with open(indexfile, mode="r", encoding="utf-8") as f:
    indexfilehtml = f.read()

footerhtml = footerhtml.replace("#date#", today)



# FAQ INDEX
    
faqfilemain = "./sources/faq/index.html"
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
    {"name": "e-shop-client", "tags": ["js", "markup", "catalog", "vuejs", "canvas"], "dirs": ["assets"], "files": [
        "bundle.js",
        "index.html"
    ], "github": True},
    {"name": "jsons-arrays", "tags": ["json", "js", "import"], "files": [
        "/css/main.css",
        "all.js",
        "index.html"
    ], "github": True},
    {"name": "users","tags": ["js", "angular", "markup"], "dirs": ["app"], "files": [], "baseUrl": "app/", "github": True},
    {"name": "laravel-sample", "tags": ["php", "api", "sqlite", "laravel", "docker"], "files": [], "github": True},
    {"name": "deezer-api-albums-php", "tags": ["php", "api", "sqlite"], "files": [], "url": "http://www.evgeniyvinokurov.byethost9.com/albums/", "github": True},
    {"name": "xmla", "tags": ["python", "js", "xml", "bottle", "catalog", "markup", "tests", "docker", "import"], "files": [], "url": "https://evgeniyvinokurov.pythonanywhere.com/catalog/", "github": True},
    {"name": "xml-engine", "tags": ["python", "js", "xml", "bottle"], "files": [], "github": True},
    {"name": "veggy-farm", "tags": ["python", "django", "catalog", "markup", "docker", "sqlite"], "files": [], "github": True},
    {"name": "base-python-app-for-web", "tags": ["python", "bottle", "xml", "vuejs", "markup"], "files": [], "url": "http://evgeniyvinokurov.pythonanywhere.com/feedback/", "github": True}
];

projectsshort = [
    "users", "xmla", "veggy-farm", "e-shop-client", "laravel-sample"
]
 

codesdir = "./common/demo/"
projectsdir = "../github/"

contentfrontproj = {}
pwis = []

for p in projects: 
    pwi = p
    with open(str(projectsdir) + "/" + p["name"] + "/README.md", mode="r", encoding="utf-8") as f:  
        lines = list(f)
        strlines = lines[1:len(lines)]            
        contentstr = "".join(strlines)
        pwi["content"] = "<h2>" + lines[0] + "</h2>" + contentstr.replace("  ", "</br>")
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
    pwis.append(pwi)

beginhtml = '''<div class='inner-brief'><p>
							Приветствую Вас на моем сайте, меня зовут Евгений, и я - программист; здесь располагаются примеры моих работ. 
						</p>
						<p>
							Если Вы хотите предложить мне работу: <a class="link" href="/faq/index.html">Faq</a>,  <a class="link" href="https://github.com/evgeniyvinokurov">Github</a>, <a class="link" href="mailto:evgeniy.vinokuroff@yandex.ru">Mail</a>, <a class="link" href="https://arkhangelsk.hh.ru/resume/8af77502ff0232226d0039ed1f373737785438">Резюме</a>
                        </p>
						<div class='inner-brief__project'>'''
endhtml = '''
        </div></div>'''

morehtml = "<h3 class='more'>More</h3><div class='tags'></div><div class='projects'>"


codesdir = "./demo/"
htmlcodes = "" 

pwihtml = []

for p in pwis: 
    pwiht = p
    file = p["name"] 
    pwiht['htmlcodes'] = ""
    if not os.path.isfile(file):
        pwiht['htmlcodes'] += "<div class='project " + " ".join(p["tags"]) + "'><p><div>" + p["content"] + "</div>"
        if "video" not in p:
            imgpath = "/demo/" + file + ".jpg"
            pwiht['htmlcodes'] += "<a href='" + imgpath + "'><img width='300px' src='" + imgpath +"'/></a>"
        else:
            videosrc = "/demo/" + file + ".mp4"
            pwiht['htmlcodes'] += "<video controls width='250'><source src='" + videosrc + "' type='video/mp4' /></video>"
        if "github" not in p:
            glink = "<a class='link' href='https://gitflic.ru/project/evgeniyvinokurov/" + file + "/'>gitflic</a>"
        else:
            glink = "<a class='link' href='https://github.com/evgeniyvinokurov/" + file + "'>github</a>"
        pwiht['htmlcodes'] += "<li>" + glink
        if len(p["files"]) > 0 or "dirs" in p:
            pwiht['htmlcodes'] += "&nbsp;&nbsp;<a class='link' href='/demo/" + file + "/" + (p["baseUrl"] if "baseUrl" in p else "") + "'>demo</a>"
        if "url" in p:
            pwiht['htmlcodes'] += "&nbsp;&nbsp;<a class='link' href='" + p["url"] + "'>demo</a>"        
        pwiht['htmlcodes'] += "</li>" + "</p></div>"
    pwihtml.append(pwiht)

pwihtmlfiltered = []

for jsp in pwihtml:
    if jsp["name"] in projectsshort:
        pwihtmlfiltered.append(jsp)

jsonps = json.dumps(pwihtmlfiltered)

for p in pwihtml: 
    morehtml += p['htmlcodes'] 

morehtml += "</div>"


preimgindexfile = "./common/index.html"
os.makedirs(os.path.dirname(preimgindexfile), exist_ok=True)
indexpreimghtml =  headerhtml + beginhtml + "<script type='text/javascript'> let projects = " + jsonps + ";</script>"+ endhtml + indexfilehtml + footerhtml

with open(preimgindexfile, mode="w", encoding="utf-8") as f:
    f.write(indexpreimghtml) 
    print("written: " + preimgindexfile)


morefile = "./common/more.html"
os.makedirs(os.path.dirname(morefile), exist_ok=True)
indexpreimghtml =  headerhtml + morehtml +  morefilehtml + footerhtml


with open(morefile, mode="w", encoding="utf-8") as f:
    f.write(indexpreimghtml) 
    print("written: " + morefile)


precssfile = "./common/css/main.css"
os.makedirs(os.path.dirname(precssfile), exist_ok=True)
shutil.copyfile("./sources/css/main.css", precssfile)
print("css copied")

