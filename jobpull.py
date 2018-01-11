#!/usr/bin/env python
import datetime as dt
import json
import urllib.request as request
from nlproc import nlproc,resume_parser
from html_builder import *



today = dt.date.today()
two_weeks_ago = today - dt.timedelta(days=cfg.days)


def json_url_load(api_url):
    json_output = json.load(request.urlopen(api_url))
    return json_output


remote_ok_result = json_url_load(cfg.jsonfeeds['remoteok'])
remotebase_result = json_url_load(cfg.jsonfeeds['remotebase'])

#############################################
#############################################


def json_build(url_input, api_name):
    if api_name == "remoteok":
        html_builder("<h3>Jobs from Json APIs</h3>", "html")
        for item in url_input:
            most_common = nlproc(item['description'])
            if item['date'] > two_weeks_ago.isoformat():
                html_builder(item['company'], "html")
                html_builder(item['position'], "html")
                html_builder(item['url'], "text")
                html_builder(str(most_common), "nltk")
    if api_name == "remotebase":
        for item in url_input['jobs']:
            most_common = nlproc(item['description'])
            if item['created_at'] or item['update_at'] > two_weeks_ago.isoformat():
                html_builder(item['company']['name'], "html")
                html_builder(item['title'], "html")
                html_builder(item['url'], "text")
                html_builder(str(most_common), "nltk")


def resume_builder():
    resume_dump = resume_parser(cfg.resume)
    most_common_resume = nlproc(resume_dump)
    html_builder(str(most_common_resume), "resume")

