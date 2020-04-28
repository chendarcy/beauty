import requests
import re
import os
import time

# 网页
web_site = 'https://www.vmgirls.com/13810.html'

# 请求网页
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}
response = requests.get(web_site, headers=headers)
html = response.text
print(html)

# 解析网页
dir_name = list(set(re.findall(r'<p><a href=".*?" alt="(.*?)" title=".*?"><img alt=".*?" src=".*?" data-src=".*?" data-nclazyload=".*?"></a></p>', html)))
urls = re.findall(r'<p><a href="(.*?)" alt=".*?" title=".*?"><img alt=".*?" src=".*?" data-src=".*?" data-nclazyload=".*?"></a></p>', html)
print(len(urls))
print(urls)
print(dir_name)

# 创建文件夹
if not os._exists(dir_name[0]):
    os.mkdir(dir_name[0])

# 保存文件
num = 1
for url in urls:
    time.sleep(1)
    with open(dir_name[0] + '\\' + str(num) + '.jpg', 'wb') as f:
        ima = requests.get(url, headers=headers)
        f.write(ima.content)
        num += 1


