import requests
from bs4 import BeautifulSoup 

page = requests.get('https://www.worldometers.info/coronavirus/country/indonesia/')

after_bs = BeautifulSoup(page.content, 'html.parser') 

find_data = after_bs.find_all(id='maincounter-wrap')  #ngambiliddarielements

#text = find_data.text

#print(text)
#print(find_data.text)
# #menampilkanhtmlsecararapih

for x in find_data: #  menampilkandatatext
    print(x.text)

#  menampilkantextyangadadimaincounter