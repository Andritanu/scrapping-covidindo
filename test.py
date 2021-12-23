import requests
from bs4 import BeautifulSoup 

page = requests.get('https://www.worldometers.info/coronavirus/country/indonesia/')

after_bs = BeautifulSoup(page.content, 'html.parser') 

find_data = after_bs.find_all(id='maincounter-wrap')  #getFromElements

#text = find_data.text

#print(text)
#print(find_data.text)
#show elements 

for x in find_data: #  show data text
    print(x.text)

#  show text ini data counter
