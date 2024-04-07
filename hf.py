import os
import shutil
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import time
import datetime
import zipfile


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

# SITEMAP

sitemapxml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'''
baseurl = "https://winegenii.tiiny.site/"


# INDEX
    
indexfilemain = "./files/index.html"
indexhtml = ""

with open(indexfilemain, mode="r", encoding="utf-8") as f:
    indexhtml = f.read()

reindexfilemain = "./index.html" 
indexfilemainhtml =  headerhtml + indexhtml + footerhtml
    
with open(reindexfilemain, mode="w", encoding="utf-8") as f:
    f.write(indexfilemainhtml) 
    print("written: " + reindexfilemain)


sitemapxml += '''<url>
    <loc>''' + baseurl + '''index.html</loc>
    <lastmod>''' + today + '''</lastmod>
  </url>'''


# FAQ
    
faqfilemain = "./files/faq/index.html"
faqhtml = ""

with open(faqfilemain, mode="r", encoding="utf-8") as f:
    faqhtml = f.read()

refaqfilemain = "./faq/index.html" 
beginhtml = "<div class='faq'>"
endhtml = "</div>"
faqfilemainhtml =  headerhtml + beginhtml + faqhtml + endhtml + footerhtml
    
os.makedirs(os.path.dirname(refaqfilemain), exist_ok=True)
with open(refaqfilemain, mode="w", encoding="utf-8") as f:
    f.write(faqfilemainhtml) 
    print("written: " + refaqfilemain)

ti_m = os.path.getmtime(faqfilemain)
tdate = datetime.datetime.utcfromtimestamp(ti_m).strftime('%Y-%m-%d')    

sitemapxml += '''<url>
    <loc>''' + baseurl + '''/faq/index.html</loc>
    <lastmod>''' + today + '''</lastmod>
  </url>'''


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
            sitemapxml += '''<url>
                <loc>''' + baseurl + '''texts/'''  + indexfile + '''</loc>
                <lastmod>''' + tdate + '''</lastmod>
            </url>'''
            htmlcontentindextexts = htmlcontentindextexts + link
            print("written: " + refile)

beginhtml = '''<p class="content-text__title">
            Тексты:
        </p>
        <ul class="text-texts list">'''
endhtml = '''
        </ul>'''
htmlcontent = textshtml + beginhtml + htmlcontentindextexts + endhtml

sitemapxml += '''<url>
                <loc>''' + baseurl + '''texts/index.html</loc>
                <lastmod>''' + today + '''</lastmod>
            </url>'''

indexfiletexts = dirparsed + "index.html" 
indexfiletextshtml = headerhtml + htmlcontent + footerhtml
with open(indexfiletexts, mode="w", encoding="utf-8") as f:
    f.write(indexfiletextshtml) 
    print("written: " + indexfiletexts)






# GALLERY
    
imgsdir = "./files/gallery2/"
beginhtml = '''<p class="content-text__title">
            Картинки:
        </p>
        <div>'''
endhtml = '''
        </div>'''
content = ""

ti_m = 0
for file in os.listdir(imgsdir):
    if os.path.isfile(imgsdir + file) and (".jpg" in file or ".png" in file):
        ti_m2 = os.path.getmtime(imgsdir + file)
        if ti_m2 > ti_m:
            ti_m = ti_m2
        reimgfile = "./gallery2/" + file
        os.makedirs(os.path.dirname(reimgfile), exist_ok=True)
        shutil.copy(imgsdir + file, reimgfile)
        print("coppied: " + reimgfile)
        img = "<a class='img' href='/gallery2/" + file + "'><img width='700px' src='/gallery2/" + file +"'/></a>"
        content = content + img

tdate = datetime.datetime.utcfromtimestamp(ti_m).strftime('%Y-%m-%d')    
reimgindexfile = "./gallery2/index.html"
indexfileimghtml =  headerhtml + beginhtml + content + endhtml + footerhtml

sitemapxml += '''<url>
                <loc>''' + baseurl + '''gallery2/index.html</loc>
                <lastmod>''' + tdate + '''</lastmod>
            </url>'''
with open(reimgindexfile, mode="w", encoding="utf-8") as f:
    f.write(indexfileimghtml) 
    print("written: " + reimgindexfile)




# CODES BACK

projects = [
    "roach-race",
    "story-linker",
    "get-your-song",
    "xmla",
    "deezer-api-albums-php"
]

current = os.path.dirname(os.path.realpath(__file__))
codesdir = os.path.dirname(current)

readmepath = "README.md"


beginhtml = '''<p class="content-text__title">
            Коды бэкенд:
        </p>
        <div class="text-codes">'''
endhtml = '''
        </div>'''

content = {}
contenthtml = ""
ti_m = 0

for p in projects:
    file = codesdir  + "/" + p + "/" + readmepath
    with open(file, mode="r", encoding="utf-8") as f:        
        ti_m2 = os.path.getmtime(file)
        if ti_m2 > ti_m:
            ti_m = ti_m2
        name = p
        lines = list(f)
        strlines = lines[1:len(lines)]            
        contentstr = "".join(strlines)
        content[name] = "<h2>" + lines[0] + "</h2>" + contentstr.replace("  ", "</br>")  + "</br></br>"
        content[name+"link"] = "</br><a class='link' href='https://gitflic.ru/project/evgeniyvinokurov/" + name + "'>gitflic</a>"
        print("processed: " + file)

for p in projects:
    imgpath = p + ".jpg"
    name = p
    file = codesdir + "/" + p + "/" + imgpath
    if os.path.isfile(file) and (".jpg" in file):
        ti_m2 = os.path.getmtime(file)
        if ti_m2 > ti_m:
            ti_m = ti_m2
        preimgfile = "./codes/" + p + ".jpg"
        os.makedirs(os.path.dirname(preimgfile), exist_ok=True)
        shutil.copy(file, preimgfile)
        print("coppied: " + preimgfile)
        preimg = "<a href='/codes/" + imgpath + "'><img width='300px' src='/codes/" + imgpath +"'/></a>"
        contenthtml = contenthtml + content[name] + preimg + content[name+"link"] + "</br></br></br></br>"

tdate = datetime.datetime.utcfromtimestamp(ti_m).strftime('%Y-%m-%d')  
preimgindexfile = "./codes/index.html"
indexpreimghtml =  headerhtml + beginhtml + contenthtml + endhtml + footerhtml

sitemapxml += '''<url>
                <loc>''' + baseurl + '''codes/index.html</loc>
                <lastmod>''' + tdate + '''</lastmod>
            </url>'''

with open(preimgindexfile, mode="w", encoding="utf-8") as f:
    f.write(indexpreimghtml) 
    print("written: " + preimgindexfile)
    
    
# CODES FRONT

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
    {"name": "jsons-arrays", "files": [
        "/css/main.css",
        "all.js",
        "index.html"
    ]},
    {"name": "tetris-like", "files": [
        "/css/main.css",
        "all.js",
        "index.html"
    ]},
]

jscodes = "./jscodes/"

current = os.path.dirname(os.path.realpath(__file__))
codesdir = os.path.dirname(current)
contentfrontproj = {}

for p in projects: 
    with open(str(codesdir) + "/" + p["name"] + "/README.md", mode="r", encoding="utf-8") as f:  
        lines = list(f)
        strlines = lines[1:len(lines)]            
        contentstr = "".join(strlines)
        contentfrontproj[p["name"]] = "<h2>" + lines[0] + "</h2>" + contentstr.replace("  ", "</br>")  + "</br></br>"
    for f in p["files"]:
        file = jscodes + "/" + p["name"] + "/" + f       
        os.makedirs(os.path.dirname(file), exist_ok=True)
        oldfile = str(codesdir) + "/" + p["name"] + "/" + f
        print("copied " + p["name"] + " " + f)
        shutil.copyfile(oldfile, file)
    oldimgfile = str(codesdir) + "/" + p["name"] + "/" + p["name"] + ".jpg"
    newimgfile = jscodes + p["name"] + ".jpg"
    shutil.copyfile(oldimgfile, newimgfile)
    print("copied " + oldimgfile)

beginhtml = '''<div class="text-codes"><p class="content-text__title">
            Коды фронтенд:
        </p>'''
endhtml = '''
        </div>'''

jscodes = "./jscodes/"
htmljscodes = "<ul class='clilist'>" 
for p in projects: 
    file = p["name"] 
    if not os.path.isfile(file):
        htmljscodes += "<p>" + contentfrontproj[file] 
        imgpath = "/" + file + ".jpg"
        htmljscodes += "<a href='/jscodes/" + imgpath + "'><img width='300px' src='/jscodes/" + imgpath +"'/></a>"
        htmljscodes += "<li>" + "<a class='link' href='https://gitflic.ru/project/evgeniyvinokurov/" + file + "/'>gitflic</a> &nbsp" + "<a class='link' href='/jscodes/" + file + "/'>demo</a></li>" + "</p>"
        htmljscodes += "<br/><br/><br/>"
htmljscodes += "</ul>"

preimgindexfile = "./jscodes/index.html"
os.makedirs(os.path.dirname(preimgindexfile), exist_ok=True)
indexpreimghtml =  headerhtml + beginhtml + htmljscodes + endhtml + footerhtml


with open(preimgindexfile, mode="w", encoding="utf-8") as f:
    f.write(indexpreimghtml) 
    print("written: " + preimgindexfile)

sitemapxml += '</urlset>'
sitemapxmlfile = "./sitemap.xml"
with open(sitemapxmlfile, mode="w", encoding="utf-8") as f:
    f.write(sitemapxml) 
    print("written: " + sitemapxmlfile)



