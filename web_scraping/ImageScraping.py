import requests
import bs4

soup = bs4.BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)').text, 'lxml')
image_info = soup.select('.mw-file-element')[1]
print(image_info['src'])
image = requests.get("https:"+image_info['src'])
f = open("sample.jpg", 'wb')
f.write(image.content)
f.close()