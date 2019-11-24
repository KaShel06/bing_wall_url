from requests import get
from bs4 import BeautifulSoup
import re
from os import chdir

#获取首张图片 js页面
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
r = get('https://cn.bing.com', headers=headers)
soup =BeautifulSoup(r.text, 'html.parser')

#link id='bglink'
#imageUrl = 'https://cn.bing.com/th?id=OHR.AtchafalayaCypress_ZH-CN0183179230_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp'
link = soup.find('link')
if link['id'] == 'bgLink':
    match = re.search(re.compile('id=(.*?)_'), link['href'])
    if match:
        imageName = match.group(1)
    imageUrl = 'https://cn.bing.com' + link['href']
print(imageUrl)

#enter may direct to the Desktop path
targetPath = input('dir path:').strip('\u202a')
if not targetPath:
    targetPath = r'C:\\Users\\acer1\\Desktop'
chdir(targetPath)

resp = get(imageUrl, headers=headers)
if imageName:
    with open(imageName + '.jpg', 'wb') as image:
        image.write(resp.content)
    print('Image Got')

    #https://stackoverflow.com/questions/42119065/pyinstaller-struct-error-unpack-requires-a-bytes-object-of-length-16
    #pyinstaller struct.error: unpack requires a bytes object of length 16
    #ico
