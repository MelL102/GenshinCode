from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import requests
import pprint

try:
    d = json.load(open('promocodes.json','r'))
    old_codes = [d[index][' EU '] for index, i in enumerate(d)]
    #print(old_codes)
except:
    old_codes = []
    print("Promocodes.json is missing! Either you deleted/moved it or you run this programm for the first time")

source = requests.get('https://www.gensh.in/events/promotion-codes').text

soup = BeautifulSoup(source, 'lxml')

table = soup.find('table')

headers = [heading.text for heading in table.find_all('th')]

table_rows = [row for row in table.find_all('tr')]

results = [{headers[index] : cell.text for index,cell in enumerate(row.find_all('td')) } for row in table_rows]

while {} in results:
    results.remove({})

eu_codes = [results[index][' EU '] for index, i in enumerate(results)]

new_codes = [codes for codes in eu_codes if codes not in old_codes]

if new_codes == []:
    print("No new codes where found")
else:
    print("The following: " + str(len(new_codes))+ " codes where found")
    for i in new_codes:
        print(i)

with open('promocodes.json', 'w') as fp:
    json.dump(results, fp, indent=4, sort_keys=True)



