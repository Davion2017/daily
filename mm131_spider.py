import requests
from lxml import etree
import os
from multiprocessing import Pool
import time

main_url = 'http://www.mm131.com/xinggan/'


def down_pic(url):
    headers = {
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    i = 1
    path = url[-9:-5]
    os.mkdir(path)
    while url:
        response = requests.get(url)
        response.encoding = 'gbk'
        html = etree.HTML(response.text)
        pic_url = html.xpath("//div[@class='content-pic']/a/img/@src")[0]
        if i == 1:
            url = main_url + html.xpath("//a[@class='page-ch']/@href")[0]
        else:
            try:
                url = main_url + html.xpath("//a[@class='page-ch']/@href")[1]
            except:
                url = None
        print(pic_url)
        os.chdir(path)
        with open(str(i) + '.jpg', 'wb') as f:
            r = requests.get(pic_url, headers=headers)
            f.write(r.content)
        os.chdir('..')
        i += 1
    print(path, '下载完成')
    print('='*60)


def get_urls(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    html = etree.HTML(response.text)
    urls = html.xpath("//dl[@class='list-left public-box']/dd/a[@target='_blank']/@href")
    if '下一页' in response.text:
        next_url = main_url + html.xpath("//dd[@class='page']/a[@class='page-en']/@href")[-2]
    else:
        next_url = None
    return urls, next_url


def main():
    # 单线程
    # url = main_url
    # while url:
    #     girl_urls, url = get_urls(url)
    #     for girl_url in girl_urls:
    #         down_pic(girl_url)

    # girl_urls, url = get_urls(main_url)
    # for girl_url in girl_urls:
    #     down_pic(girl_url)

    # 多进程
    # pool = Pool()
    # girl_urls, url = get_urls(main_url)
    # pool.map(down_pic, girl_urls)
    url = main_url
    i = 1
    while url:
        girl_urls, url = get_urls(url)
        pool = Pool()
        pool.map(down_pic, girl_urls)
        print('第%s页下载完成'%i)
        i += 1
        print()
        print('+'*60)
        time.sleep(3)


if __name__ == '__main__':
    main()
