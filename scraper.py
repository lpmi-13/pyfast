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

def getNationality(url):
    Georgian = re.search('Georgia', url)
    if (Georgian):
	return 'Georgian'
    else:
	return re.search('List_of_(.+?)_records', url).group(1)

for link in record_links:
    national_link = link.get('href', None)
    national_record_page = urllib.urlopen(base_url + national_link).read()
    starting_el = BeautifulSoup(national_record_page, 'html.parser')
    table = starting_el.find('span', {'id':'Men'})
    mens_table = table.find_next('table', class_='wikitable')

    table = starting_el.find('span', {'id':'Women'})
    womens_table = table.find_next('table', class_='wikitable')

    print getNationality(national_link)
    for distance in race_array:
        men_race_distance = mens_table.find('a', href='/wiki/'+ distance)
	women_race_distance = womens_table.find('a', href='/wiki/'+distance)

	print distance
	print 'Men'
        try:
	    men_race_time = men_race_distance.find_parent('td').find_next_sibling()
            try:
                print re.match('\S+', men_race_time.text).group(0)
            except:
                print 'no time found'
	except:
	    print 'no time found'

	print 'Women'
	try:
	    women_race_time = women_race_distance.find_parent('td').find_next_sibling()
	    try:
		print re.match('\S+', women_race_time.text).group(0)
	    except:
		print 'no time found'
	except:
	    print 'no time found'
