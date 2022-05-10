import re
import requests

def download_audio(url_list):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}

    i = 1
    for url in url_list:
        url = url.replace('\/', '/')
        data = requests.get(url=url, headers=header, timeout=20).content

        path = 'D:/zz/小迟讲道集/第' + str(i) + '节.mp3'
        with open(path, 'wb') as fp:
            fp.write(data)
            print(i, '下载成功')
        i = i + 1


def get_audio_link(url):
    html = requests.get(url).text
    # print(html)

    list = []
    ex = 'playurl":"(.*?)"'
    list += re.findall(ex, html, re.S)
    print(list)

    return list


if __name__ == "__main__":
    url = 'http://api.kuaiyuhudong.cn/api/web/share/postor.php?aid=2912&sid=81188&bundleid='

    url_list = get_audio_link(url)
    download_audio(url_list)


# pay attention: when you want to download XiaoChi-Series audio,
# you should change the url in the main function and the folder name in the download_audio function
# before download, make sure the folder exists



