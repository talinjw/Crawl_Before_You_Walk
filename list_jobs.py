import requests
import bs4
from selenium import webdriver
import pandas as pd
import time
from pprint import pprint

searchWhat = 'jobs?q=' + 'analyst'
searchWhere = '&l=' + 'Bay Area, CA'
searchQuery = searchWhat + searchWhere
print(searchQuery)

url = 'https://www.indeed.com/' + searchQuery

#Open Chrome and navigate to Indeed.com
browser = webdriver.Chrome()
browser.get(url)
#res = requests.get(url)
html = browser.page_source


soup = bs4.BeautifulSoup(html, 'html.parser')
print(soup.prettify())

def get_job_title(soup):
    jobs = []
    for a in soup.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            jobs.append(a["title"])
    return(jobs)

all_jobs = get_job_title(soup)
print('Print # of jobs: ' + str(len(all_jobs)))
pprint(all_jobs)


def get_companies(soup): 
    companies = []
    company = soup.find_all(name='span', attrs={'class':'company'})
    
    for b in company:
        companies.append(b.text.strip())

    return(companies)

all_companies = get_companies(soup)
print('Print # of companies: ' + str(len(all_companies)))
pprint(all_companies)


def get_locations(soup):
    locations = []
    spans = soup.findAll('span', attrs={'class': 'location'})
    for span in spans:
        locations.append(span.text)
    return(locations)

all_locations = get_locations(soup)
print('Print # of locations: ' + str(len(all_locations)))
pprint(all_locations)


def get_summary(soup):
    summaries = []
    spans = soup.findAll('span', attrs={'class': 'summary'})
    for span in spans:
        summaries.append(span.text.strip())
    return(summaries)

all_summaries = get_summary(soup)
print('Print # of summaries: ' + str(len(all_summaries)))
pprint(all_summaries)

