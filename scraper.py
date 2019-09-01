import requests
from bs4 import BeautifulSoup
# URL is basically our amazon item
URL = "https://www.amazon.co.uk/Bluetooth-Anker-SoundCore-Portable-Playtime-Black/dp/B01HTH3C8S/ref=sr_1_3?keywords=bluetooth+speaker&qid=1567340467&s=gateway&sr=8-3"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'} #basically our browser info, my user agent on google should give me info for that
page = requests.get(URL, headers=headers) #requests the page with the URL and header variable given at the top
soup = BeautifulSoup(page.content, 'html.parser') #soup can give us the entire code from a website, just like view code source from f12
#print(soup.prettify()) #prints the entire code from a website
title = soup.find(id="productTitle").get_text()
print(title.strip())
