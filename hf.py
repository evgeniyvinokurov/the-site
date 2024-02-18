import os
import shutil
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import time
import datetime


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
faqfilemainhtml =  headerhtml + faqhtml + footerhtml
    
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
dirparsed = "./texts/"

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

        refilehtml = headerhtml + html + footerhtml
        os.makedirs(os.path.dirname(refile), exist_ok=True)
        with open(refile, mode="w", encoding="utf-8") as f:
            f.write(refilehtml) 
            link = "<li class='link'><span>" + getttile(dirtexts + indexfile) + "</span> <a href='" + indexfile  + "'>-></a></li>"
            sitemapxml += '''<url>
                <loc>''' + baseurl + '''texts/'''  + indexfile + '''</loc>
                <lastmod>''' + tdate + '''</lastmod>
            </url>'''
            htmlcontentindextexts = htmlcontentindextexts + link
            print("written: " + refile)

beginhtml = '''<p class="content-text__title">
            Тексты:
        </p>
        <ul class="text-texts">'''
endhtml = '''
        </ul>'''
htmlcontent = beginhtml + htmlcontentindextexts + endhtml

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




# CODES

iprecodesdir = "./files/precodes/imgs/"
precodesdir = "./files/precodes/md/"


beginhtml = '''<p class="content-text__title">
            Коды:
        </p>
        <div class="text-codes">'''
endhtml = '''
        </div>'''

content = {}
contenthtml = ""
ti_m = 0

for file in os.listdir(precodesdir):
    if os.path.isfile(precodesdir + file) and (".md" in file):
        with open(precodesdir + file, mode="r", encoding="utf-8") as f:        
            ti_m2 = os.path.getmtime(precodesdir + file)
            if ti_m2 > ti_m:
                ti_m = ti_m2
            name = (Path(precodesdir + file)).stem
            content[name] = f.read().replace("  ", "</br>")  + "</br></br>"
            content[name+"link"] = "</br><a href='https://gitflic.ru/project/evgeniyvinokurov/" + name + "'>"+ name +"</a>"
            print("processed: " + precodesdir +  file)

for file in os.listdir(iprecodesdir):
    if os.path.isfile(iprecodesdir + file) and (".jpg" in file):
        ti_m2 = os.path.getmtime(iprecodesdir + file)
        if ti_m2 > ti_m:
            ti_m = ti_m2
        name = (Path(precodesdir + file)).stem
        preimgfile = "./codes/" + file
        os.makedirs(os.path.dirname(preimgfile), exist_ok=True)
        shutil.copy(iprecodesdir + file, preimgfile)
        print("coppied: " + preimgfile)
        preimg = "<a href='/codes/" + file + "'><img width='300px' src='/codes/" + file +"'/></a>"
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


sitemapxml += '</urlset>'
sitemapxmlfile = "./sitemap.xml"
with open(sitemapxmlfile, mode="w", encoding="utf-8") as f:
    f.write(sitemapxml) 
    print("written: " + sitemapxmlfile)