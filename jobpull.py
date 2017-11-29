#!/usr/bin/env python
import json
import urllib.request as request
import feedparser
import datetime as dt
from bs4 import BeautifulSoup as bs
today = dt.date.today()

############################################
# user defined vars
url = {
    'remoteok': 'https://remoteok.io/remote-jobs.json',
    'stackDevops': "https://stackoverflow.com/jobs/feed?tl=devops+automation+puppet+python+",
    'stackSecurity': "https://stackoverflow.com/jobs/feed?tl=security+soc+",
    'weworkremotely': "https://weworkremotely.com/categories/6-devops-sysadmin/jobs.rss",
    'remotebase': "http://api.remotebase.io/companies?fully_remote=true&hiring_regions=Worldwide",
    'indeedAutomation': "http://rss.indeed.com/rss?q=automation&l=Remote&sort=date",
    'indeedSecurity': "https://www.indeed.com/jobs?q=devops+OR+security&l=Remote&sort=date",
    'usajobs': "https://api.usa.gov/jobs/search.json?query=it+jobs+in+nj"
}
two_weeks_ago = today - dt.timedelta(days=17)
maxdesc = 900  # how many characters to print of the description
############################################
# do not modify below

remote_ok_result = json.load(request.urlopen(url['remoteok']))
url_stack = feedparser.parse(url['stackDevops'])
url_stack_sec = feedparser.parse(url['stackSecurity'])
url_wework = feedparser.parse(url['weworkremotely'])
open_usa_result = json.load(request.urlopen(url['usajobs']))
remote_base_result = json.load(request.urlopen(url['remotebase']))
url_indeed = feedparser.parse(url['indeedAutomation'])
url_indeed_sec = feedparser.parse(url['indeedSecurity'])
start = 0


def remoteokcall():  # Remote Ok Function
    print("Remote Jobs from Remoteok.io")
    print("============================")
    for item in remote_ok_result:
        if item['date'] > two_weeks_ago.isoformat():
            print('Company Name:', item['company'])
            print('Title:', item['position'])
            print('Post date:', item['date'][:10])
            keyw = str(item['tags'])
            print('Keywords:', keyw.replace("'", ""))
            desc = str(item['description'])
            soup = bs(desc, 'html.parser')
            print('\n')
            print('Description:', soup.get_text()[start:start+maxdesc] + '\n')
            print('Apply Here:', item['url'])
            print('\n')
            print('##########')


def stackdevopsjobs():  # Stack RSS Function
    print('Remote Devops Jobs from Stack Overflow')
    print("============================")
    for post in url_stack.entries:
        if post.date > two_weeks_ago.isoformat():
            print('Title: ', post.title)
            print('Post date: ', post.date[:10])
            print('\n')
            desc = str(post.description)
            soup = bs(desc, 'html.parser')
            print('Description: ', soup.get_text()[start:start+maxdesc] + '\n')
            print('Apply Here: ', post.link)
            print('\n')
            print('##########')


def stacksecurityjobs():  # Stack RSS Function
    print("Remote Security Jobs from Stack Overflow")
    print("============================")
    for post in url_stack_sec.entries:
        if post.date > two_weeks_ago.isoformat():
            print('Title: ', post.title)
            print('Post date: ', post.date[:10])
            print('\n')
            desc = str(post.description)
            soup = bs(desc, 'html.parser')
            print('Description: ', soup.get_text()[start:start+maxdesc] + '\n')
            print('Apply Here: ', post.link)
            print('\n')
            print('##########')


def weworkjobs():
    print("We Work Remotley Jobs")
    print("========================")
    for post in url_wework.entries:
        if post.published > two_weeks_ago.isoformat():
            print('Title: ', post.title)
            print('Post date: ', post.published[:17])
            print('\n')
            desc = str(post.description)
            soup = bs(desc, 'html.parser')
            print('Description: ', soup.get_text()[start:start+maxdesc] + '\n')
            print('Apply Here: ', post.link)
            print('\n')
            print('##########')


def usajobsreturn():  # USA jobs Function
    print("Wichita Jobs USA Jobs")
    print("============================")
    for item in open_usa_result:
        print('Company Name:', item['organization_name'])
        print('Title:', item['position_title'])
        print('\n')
        desc = str(item['description'])
        soup = bs(desc, 'html.parser')
        print('Description:', soup.get_text()[start:start + maxdesc] + '\n')
        print('End Date: ', item['end_date'])
        print('Apply Here: ', item['url'])
        print('\n')
        print('##########')


def indeedrssjobs():  # indeed RSS Function
    print("Remote devops Jobs from Indeed")
    print("============================")
    for post in url_indeed.entries:
        print('Title: ', post.title)
        print('Post date: ', post.published[:17])
        print('\n')
        desc = str(post.description)
        soup = bs(desc, 'html.parser')
        print('Description: ', soup.get_text()[start:start + maxdesc] + '\n')
        print('Apply Here: ', post.link)
        print('\n')
        print('##########')


def indeedsecuirtyjobs():  # indeed RSS Function
    print("Remote Security Jobs from Indeed")
    print("============================")
    for post in url_indeed_sec .entries:
        print('Title: ', post.title)
        print('Post date: ', post.published[:17])
        print('\n')
        desc = str(post.description)
        soup = bs(desc, 'html.parser')
        print('Description: ', soup.get_text()[start:start + maxdesc] + '\n')
        print('Apply Here: ', post.link)
        print('\n')
        print('##########')


def remotebasecall():  # Remote Base Function
    print("Jobs From RemoteBase")
    print("=================================")
    for item in remote_base_result['companies']:
        if item['updated_at'] or item['created_at'] > two_weeks_ago.isoformat():
            print('Company Name:', item['name'])
            print('Job function:', item['short_description'])
            print('\n')
            desc = str(item['description'])
            soup = bs(desc, 'html.parser')
            print('Description:', soup.get_text()[start:start + maxdesc] + '\n')
            print('Apply Here: ', item['job_page'])
            print('\n')
            print('##########')

if __name__ == "__main__":
    print("RemoteOK jobs" + '\n')
    remoteokcall()
    print("Stack jobs" + '\n')
    stackdevopsjobs()
    print("Stack security jobs" + '\n')
    stacksecurityjobs()
    print('Wework jobs' + '\n')
    weworkjobs()
    print('Indeed automation jobs' + '\n')
    indeedrssjobs()
    print('Indeed security jobs' + '\n')
    indeedsecuirtyjobs()
    print('Remotebase' + '\n')
    remotebasecall()


