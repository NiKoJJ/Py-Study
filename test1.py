from bs4 import BeautifulSoup
import requests
import re
url = 'http://www.cntour.cn/'
str = requests.get(url)
soup = BeautifulSoup(str.text, 'lxml')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
for item in data:
    result = dict(title=item.get_text(), link=item.get('href'), ID=re.findall('\d+', item.get('href')))
    print(result)