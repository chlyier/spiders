import re
import urllib.parse
import json
import requests



def get_small_img_url(url):
    header = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36'}
    small_img_url_list = []
    page_html = requests.get(url, headers=header).text
    ex = '<a class="preview" href="(.*?)"'
    small_img_url_list += re.findall(ex, page_html, re.S)
    return small_img_url_list


def get_img(small_img_url_list):
    header = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36'}
    for i in range(len(small_img_url_list)):
        x = small_img_url_list[i].split('/')[-1]  # 获取最后一个斜杠后的字符串
        a = x[0] + x[1]  # 获取字符串的前两位
        img_url = 'https://w.wallhaven.cc/full/' + a + '/wallhaven-' + x + '.jpg'
        code = requests.get(url=img_url, headers=header).status_code
        if code == 404:
            img_url = 'https://w.wallhaven.cc/full/' + a + '/wallhaven-' + x + '.png'
        img_data = requests.get(url=img_url, headers=header, timeout=20).content
        img_name = img_url.split('-')[-1]
        img_path = 'D:/wallhaven/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功')


def main():
    for page_index in range(1, 3):
        print("Page", page_index, ":")
        url = 'https://wallhaven.cc/toplist?page=' + str(page_index)
        small_img_url_list = get_small_img_url(url)
        get_img(small_img_url_list)

main()