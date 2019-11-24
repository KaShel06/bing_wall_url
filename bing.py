from requests import get
from bs4 import BeautifulSoup
import re
from os import chdir

#获取首张图片 js页面
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
r = get('https://cn.bing.com', headers=headers)
soup =BeautifulSoup(r.text, 'html.parser')

link = soup.find('link')
if link['id'] == 'bgLink':
    match = re.search(re.compile('id=(.*?)_'), link['href'])
    if match:
        imageName = match.group(1)
    imageUrl = 'https://cn.bing.com' + link['href']
print(imageUrl)
resp = get(imageUrl, headers=headers)
targetPath = r'C:\\Users\\acer1\\Desktop'
chdir(targetPath)
if imageName:
    with open(imageName + '.jpg', 'wb') as image:
        image.write(resp.content)
    print('Image Got')