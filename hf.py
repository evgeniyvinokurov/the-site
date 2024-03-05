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



# CODES

beginhtml = '''<div class="text-codes">'''
endhtml = '''
        </div>'''

jscodes = "./jscodes/"
htmljscodes = "<ul class='clilist'>" 
for file in os.listdir(jscodes):
	htmljscodes += "<li>" + file + "<a class='link' href='/jscodes/" + file + "/'>-></a></li>"
htmljscodes += "</ul>"

preimgindexfile = "./index.html"
indexpreimghtml =  headerhtml + beginhtml + htmljscodes + endhtml + footerhtml


with open(preimgindexfile, mode="w", encoding="utf-8") as f:
    f.write(indexpreimghtml) 
    print("written: " + preimgindexfile)





