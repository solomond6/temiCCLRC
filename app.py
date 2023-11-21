from flask import Flask, jsonify, request, render_template
import urllib.request as urllib2
import http.cookiejar as cookielib
import xmltodict
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template ("index.html")

@app.route("/getData", methods=['GET', 'POST'])
def get_data():
    content = file_get_contents("http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=109-02-088")
    content_dict = xmltodict.parse(content.strip())
    return jsonify(content_dict)


def file_get_contents(url):
    url = str(url).replace(" ", "+") # just in case, no space in url
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    req = urllib2.Request(url, headers=hdr)
    try:
        page = urllib2.urlopen(req)
        return page.read()
    except urllib2.HTTPError as e:
        print(e.fp.read())
    return ''


if __name__ == '__main__':
    app.run()