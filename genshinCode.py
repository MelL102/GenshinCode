# Module importieren
import requests
import csv
from bs4 import BeautifulSoup

source = requests.get('https://www.gensh.in/events/promotion-codes').text

soup = BeautifulSoup(source, 'lxml')

table = soup.find('table')

# print(table.prettify())
table_body = table.find('tbody')
#print(table_body)
rows = table_body.find_all('tr')
#print(rows)
data = []

for row in rows:
    cols = row.find_all('td')
    data.append(cols)

code = ""

file = open("promocodes.txt","a+")
try:
    old_promos = open("promocodes.txt","r")
    content_list = old_promos.read().splitlines()
except:
    print("No old Promocodes where found \n")
    content_list = []

count = 0
new_codes = []
for item in data:
    code = item[2]
    code = str(code)[5 : -6]
    try:
        b = content_list.index(code)
        continue
    except:
        file.write(code+"\n")
        count = count+1
        new_codes.append(code)

if count > 0:
    print(str(count)+" new codes that can be redeemed where found:\n")
    for code in new_codes:
        print(code+"\n")
else:
    print("No new codes where found")
