import requests
from lxml import etree
import os

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
main_url = 'https://cubingchina.com'

def open_url(url):
    response = requests.get(url, headers=headers)
    return response.text


def get_person_index_urls(html):
    html = etree.HTML(html)
    result = html.xpath('//tr/td/a/@href')
    urls = []
    for url in result[::2]:
        urls.append(main_url + url)
    return urls


def get_icon(url):
    html = open_url(url)
    html =etree.HTML(html)
    wca_id = html.xpath("//span[@class='info-value']/text()")[3]
    try:
        icon_url = html.xpath("//div[@class='text-center']/a/img/@src")[0]
        r = requests.get(icon_url, headers=headers)
        os.chdir('./icon')
        with open(wca_id+'.jpeg', 'wb') as f:
            f.write(r.content)
        os.chdir('..')
    except:
        print(wca_id ,'No picture')


def get_next_url(html):
    html = etree.HTML(html)
    try:
        next_url = html.xpath("//li[@class='next']/a/@href")[0]
        return main_url + next_url
    except:
        return None


def main():
    url = 'https://cubingchina.com/results/person?page=167'
    page = 1
    while url != None:
        html = open_url(url)
        index_urls = get_person_index_urls(html)
        url = get_next_url(html)
        for index_url in index_urls:
            get_icon(index_url)
        print('第%s页下载完成'%page)
        page += 1

if __name__ == '__main__':
    main()