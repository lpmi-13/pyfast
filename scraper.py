import urllib
from bs4 import BeautifulSoup
import re

race_array = ['100_metres', '200_metres', '400_metres', '800_metres', '1500_metres', '3000_metres', '5000_metres', '10,000_metres', 'Half_marathon', 'Marathon']

record_list_url = 'https://en.wikipedia.org/wiki/National_records_in_athletics'
base_url = 'https://en.wikipedia.org'

record_list_html = urllib.urlopen(record_list_url).read()

recordsoup = BeautifulSoup(record_list_html, 'html.parser')
recordtable = recordsoup.find('table', class_="multicol")

record_links = recordtable.find_all('a')

for link in record_links:
    national_link = link.get('href', None)
    national_record_page = urllib.urlopen(base_url + national_link).read()
    starting_el = BeautifulSoup(national_record_page, 'html.parser')
    table = starting_el.find('span', {'id':'Men'})
    mens_table = table.find_next('table', class_='wikitable')
    race_distance = mens_table.find('a', href='/wiki/100_metres')
    race_time = race_distance.find_parent('td').find_next_sibling()
    print re.match('\S+', race_time.text).group(0)
