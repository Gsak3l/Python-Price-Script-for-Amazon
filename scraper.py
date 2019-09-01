import requests
from bs4 import BeautifulSoup
URL = "https://www.amazon.com/Enhanced-Splashproof-Portable-Bluetooth-Radiator/dp/B010OYASRG/ref=sxin_2_ac_d_pm?ac_md=2-0-VW5kZXIgJDMw-ac_d_pm&keywords=bluetooth+speaker&pd_rd_i=B010OYASRG&pd_rd_r=7e9d0246-6e5d-4b6f-a9bb-fa4c4d1aca95&pd_rd_w=EBj63&pd_rd_wg=x2f2N&pf_rd_p=eeff02d5-070a-45ea-a79e-d591974b877e&pf_rd_r=3ESD78PWJSG42ZBPTEYD&psc=1&qid=1567336060&s=gateway"
#URL is basically our amazon item
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'} #basically our browser info, my user agent on google should give me info for that
page = requests.get(URL, headers=headers) #requests the page with the URL and header variable given at the top
soup = BeautifulSoup(page.content, 'html.parser') #soup can give us the entire code from a website, just like view code source from f12
#print(soup.prettify()) #prints the entire code from a website
title = soup.find(id="productTitle")
print(title)
