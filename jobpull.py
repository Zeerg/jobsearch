#!/usr/bin/env python
#Requires python 2.7
#Import These Modules
import json
import urllib2
import feedparser
import datetime as dt

#Setup date variables
today = dt.date.today()
two_weeks_ago = today - dt.timedelta(days=14)

#URL Dict
#Need to seperate this out for loop
url = {'remoteok': "https://remoteok.io/remote-jobs.json",
       'stackrss': "http://stackoverflow.com/jobs/feed?r=True&tl=sysadmin+",
       'weworkremotely': "https://weworkremotely.com/categories/6-devops-sysadmin/jobs.rss",
       'remotebase': "http://api.remotebase.io/companies?is_hiring=true&hiring_regions=United%20States",
       'indeed': "http://rss.indeed.com/rss?q=Linux&l=Remote&sort=date",
       'usajobs': "https://api.usa.gov/jobs/search.json?query=it+jobs+in+wichita+ks",
       }

#remoteok api
remote_ok_result = json.load(urllib2.urlopen(url['remoteok']))

#remote base api
remote_base_result = json.load(urllib2.urlopen(url['remotebase']))

#wichita KS jobs
open_usa_result = json.load(urllib2.urlopen(url['usajobs']))

#stackrss
url_stack = feedparser.parse(url['stackrss'])

#we work remotely rss
url_wework = feedparser.parse(url['weworkremotely'])

#indeed rss
url_indeed = feedparser.parse(url['indeed'])

#Remote Ok Function
def remoteokcall():

    print "New Remote Jobs from Remoteok.io"
    print "============================"
    for item in remote_ok_result:
        if item['date'] > two_weeks_ago.isoformat():
            print 'Company Name:', item['company']
            print 'Title:', item['position']
            print 'Apply Here: ', item['url'] + '\n'

remoteokcall()

def usajobsreturn():

    print "Wichita Jobs USA Jobs"
    print "============================"
    for item in open_usa_result:
        print 'Company Name:', item['organization_name']
        print 'Title:', item['position_title']
        print 'End Date: ', item['end_date']
        print 'Apply Here: ', item['url'] + '\n'

usajobsreturn()

#Stack RSS Function
def stackrssjobs():

    print "New Remote Jobs from Stack Overflow"
    print "============================"

    for post in url_stack.entries:
        if post.date > two_weeks_ago.isoformat():
            print 'Title: ', post.title
            print 'Apply Here: ', post.link + '\n'

stackrssjobs()

#We work Remotley Function Seriously lame that iso is not used.
def weworkjobs():

    print "New We Work Remotley Jobs"
    print "========================"

    for post in url_wework.entries:
        #stupid workaround for http://bugs.python.org/issue6641
        old_published_date = post.published
        published_date = old_published_date[:25]
        published_date_iso = dt.datetime.isoformat(dt.datetime.strptime(published_date, '%a, %d %b %Y %H:%M:%S'))
        #Finish stupid workaround
        if published_date_iso > two_weeks_ago.isoformat():
                print "Title: ", post.title
                print "Apply Here: ", post.link + "\n"

weworkjobs()

#Stack RSS Function
def indeedrssjobs():

    print "New Remote Jobs from Indeed"
    print "============================"

    for post in url_indeed.entries:
        print 'Title: ', post.title
        print 'Apply Here: ', post.link + '\n'

indeedrssjobs()

#Remote Base Function

def remotebasecall():

    print "Possibilities From RemoteBase"
    print "================================="
    for item in remote_base_result['companies']:
        if item['updated_at'] or item['created_at'] > two_weeks_ago.isoformat():
            print 'Company Name:', item['name']
            print 'Apply Here: ', item['website'] + '\n'

remotebasecall()