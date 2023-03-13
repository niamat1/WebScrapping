#web scraper
from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_a49e0d71-0a45-4fde-ad0a-748411bef304_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
source = soup.find_all('div', class_='_2kHMtA')
with open('products.csv', 'w',encoding='utf8', newline='') as f:
    head = ['Name','price','preprice','offer','delivery']
    writer = csv.writer(f)
    writer.writerow(head)
    for list in source:
        name = list.find('div', class_='_4rR01T').text
        price = list.find('div', class_='_30jeq3').text.replace('₹','Rupe = ')
        previousPrice = list.find('div', class_='_3I9_wc').text.replace('₹','Rupe = ')
        offer = list.find('div', class_='_3Ay6Sb').text
        delivery = list.find('div', class_='_2Tpdn3').text
        info = [name, price ,previousPrice , offer , delivery]
        writer.writerow(info)




