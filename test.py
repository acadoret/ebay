from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
from api import ebayapi

Keywords = input("Enter your keyword/s \n")
api = finding(appid=ebayapi, siteid='EBAY-FR', config_file=None)
api_req = { 'keywords': Keywords, 'outputSelector': 'SellerInfo'}

res = api.execute('findItemsByKeywords', api_req)
soup = BeautifulSoup(res.content, 'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

print()
print()

for item in items:
    cat = item.categoryname.string.lower()
    title = item.title.string.lower().strip()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()
    seller = item.serrerusername.text.lower()
    