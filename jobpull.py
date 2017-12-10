#!/usr/bin/env python
import json
import urllib.request as request
import feedparser as fp
import datetime as dt
import config as cfg
import nltk
from json2html import *
from bs4 import BeautifulSoup as bs


stopwords = nltk.corpus.stopwords.words('english')
today = dt.date.today()
two_weeks_ago = today - dt.timedelta(days=17)
start = 0



def json_url_load(api_url):
    json_output = json.load(request.urlopen(api_url))
    return json_output


remote_ok_result = json_url_load(cfg.jsonfeeds['remoteok'])
remotebase_result = json_url_load(cfg.jsonfeeds['remotebase'])

#############################################
#############################################


def clean_html():
    with open('output.html', 'w') as newpull:
        newpull.write("<!doctype html>")
        newpull.write('<html lang = "en">')
        newpull.write("<head>")
        newpull.write('<meta charset = "utf-8">')
        newpull.write("<title > Find Da Job</title>")
        newpull.write("</head>")
        newpull.write("<body>")
        newpull.close()


def html_builder(result_write, placement):
    with open('output.html', 'a') as myFile:
        if placement == "text":
            myFile.write("Apply Here: ")
            myFile.write(json2html.convert(result_write).encode('ascii', 'ignore').decode('ascii'))
            myFile.write('</br>')
            myFile.close()
        if placement == "html":
            myFile.write(result_write)
            myFile.write('</br>')
            myFile.close()
        if placement == "nltk":
            myFile.write("Most Common Words: ")
            myFile.write(json2html.convert(result_write).encode('ascii', 'ignore').decode('ascii'))
            myFile.write('</br>')
            myFile.close()


def json_build(url_input):
    html_builder("<h3>Jobs From RemoteOk</h3>", "html")
    for item in url_input:
        if item['date'] > two_weeks_ago.isoformat():
            allwords = nltk.tokenize.word_tokenize(item['description'])
            allWordDist = nltk.FreqDist(w.lower() for w in allwords)
            stopwords = nltk.corpus.stopwords.words('english')
            allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allwords if w not in stopwords)
            mostCommon = str(allWordExceptStopDist.most_common(10))
            html_builder(item['company'], "html")
            html_builder(item['position'], "html")
            html_builder(item['url'], "text")
            html_builder(mostCommon, "nltk")


def json_build_rb(url_input):
    html_builder("<h3>Compaines From Remote Base</h3>", "html")
    for item in url_input['companies']:
        if item['updated_at'] or item['created_at'] > two_weeks_ago.isoformat():
            html_builder(item['website'], "text")

def close_html():
    with open('output.html', 'a') as newpull:
        newpull.write("</body>")
        newpull.write("</html>")
        newpull.close()