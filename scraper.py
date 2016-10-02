import urllib
from bs4 import BeautifulSoup
import re

record_list_url = 'https://en.wikipedia.org/wiki/National_records_in_athletics'

record_list_html = urllib.urlopen(record_list_url).read()

recordsoup = BeautifulSoup(record_list_html, 'html.parser')
recordtable = recordsoup.find('table', class_="multicol")

record_links = recordtable.find_all('a')

for link in record_links:
    print link.get('href', None)
