#!/usr/bin/env python
import config as cfg
import datetime as dt
import json
import urllib.request as request
from json2html import *
from nlproc import *


today = dt.date.today()
two_weeks_ago = today - dt.timedelta(days=cfg.days)


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
            myFile.write('</br>')
            myFile.close()
        if placement == "resume":
            myFile.write("<h3>Current Resume Keywords</h3>")
            myFile.write(result_write)
            myFile.write('</br>')
            myFile.close()


def json_build(url_input, api_name):
    if api_name == "remoteok":
        html_builder("<h3>Jobs from Json APIs</h3>", "html")
        for item in url_input:
            if item['date'] > two_weeks_ago.isoformat():
                html_builder(item['company'], "html")
                html_builder(item['position'], "html")
                html_builder(item['url'], "text")
                most_common = nlproc(item['description'])
                html_builder(most_common, "nltk")
    if api_name == "remotebase":
        for item in url_input['jobs']:
            if item['created_at'] or item['update_at'] > two_weeks_ago.isoformat():
                html_builder(item['company']['name'], "html")
                html_builder(item['title'], "html")
                html_builder(item['url'], "text")
                most_common = nlproc(item['description'])
                html_builder(most_common, "nltk")


def resume_builder():
    resume_dump = resume_parser(cfg.resume)
    most_common_resume = nlproc(resume_dump)
    html_builder(most_common_resume, "resume")


def close_html():
    with open('output.html', 'a') as newpull:
        newpull.write("</body>")
        newpull.write("</html>")
        newpull.close()