import requests
from bs4 import BeautifulSoup
import smtplib
import time
#URL is basically our amazon item
URL = "https://www.amazon.co.uk/Bluetooth-Anker-SoundCore-Portable-Playtime-Black/dp/B01HTH3C8S/ref=sr_1_3?keywords=bluetooth+speaker&qid=1567340467&s=gateway&sr=8-3"
#basically our browser info, my user agent on google should give me info for that
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
#requests the page with the URL and header variable given at the top
page = requests.get(URL, headers=headers)
#soup can give us the entire code from a website, just like view code source from f12
soup = BeautifulSoup(page.content, 'html.parser')

def check_price():
    #print(soup.prettify()) #prints the entire code from a website
    title = soup.find(id="productTitle").get_text() #the title of the object i want to buy
    price = soup.find(id="priceblock_ourprice").get_text() #the price of the object i want to buy
    print(title.strip())  #i print the title
    convertPrice = float(price[0:3]) # iam taking the first 3 digits of a price, and i convert it to a float. It was string by default
    print(convertPrice)  #i print the price, strip() kills the extra spaces
    if(convertPrice < 200):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #ehlo is a command sent by an email server to identify itself when connecting to another email
    server.starttls() #this encrypts our connection
    server.ehlo()
    server.login('username@gmail.com', 'thisIsApassword') #our mail information
    subject = 'Price of your item fell down!' #subject of the email
    body = 'check the amazon link to buy this product https://www.amazon.co.uk/Bluetooth-Anker-SoundCore-Portable-Playtime-Black/dp/B01HTH3C8S/ref=sr_1_3?keywords=bluetooth+speaker&qid=1567340467&s=gateway&sr=8-3' #body of the email
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail
    (
        'username@gmail.com', #username of the email that we use to sent the alert
        'anothermail@gmail.com', #email reciever
        msg
    )
    print('Action Completed') #just a random message that tells us if this worked
    server.quit() #quits from the server

while(True): #this basically runs once, and then pauses the execution for 1 hour 60*60 = 1 hour minutes * seconds
        check_price()
        time.sleep(60*60)

#this project is over