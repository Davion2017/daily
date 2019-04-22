'''
    功能：爬取粗饼网所有人三阶单次成绩
    作者：Davion
    版本：V1.0
    日期：2018/03/12
'''

import requests
from bs4 import BeautifulSoup
import csv

main_url = 'https://cubingchina.com'


def get_html(url):
    '''
        根据url返回相应的html对象
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    # print(response)
    return html


def get_soup(html):
    '''
        根据HTML返回beautifulsoup对象
    '''
    soup = BeautifulSoup(html, 'lxml')
    return soup


def get_rank_list(soup):
    '''
        使用beautifulsoup解析网页，取得选手信息
        返回选手信息列表
    '''
    rank_text_list = soup.find('table', {'class': 'table table-bordered table-condensed table-hover table-boxed'})
    rank_text_list = rank_text_list.find_all('tr')[1:]
    rank_list = []
    for rank_text in rank_text_list:
        rank_text = rank_text.find_all('td')
        rank = rank_text[1].extract().text
        name = rank_text[2].extract().text
        result = rank_text[4].extract().text
        competitive = rank_text[5].extract().text
        date = rank_text[6].extract().text
        item = (rank, name, result, competitive, date)
        rank_list.append(item)
    return rank_list


def writer_file(rank_list, flag=''):
    '''
        写入csv文件
    '''
    header = ('排名', '姓名', '成绩', '比赛', '日期')
    with open('333_single_China.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        if flag == 'first':
            writer.writerow(header)
        for rank in rank_list:
            writer.writerow(rank)


def get_next_url(soup):
    '''
        获取下一页地址
    '''
    url_text = soup.find('li', {'class': 'next'})
    url_text = url_text.find('a')
    url = main_url + url_text.get('href')
    return url


def main():
    start_url = 'https://cubingchina.com/results/rankings'

    html = get_html(start_url)
    soup = get_soup(html)
    # print(soup)
    # 排名写入文件
    rank_list = get_rank_list(soup)
    # print(rank_list)
    writer_file(rank_list, 'first')
    print('第1页下载完成')
    # 获取下一页url
    next_url = get_next_url(soup)
    # 获取最后一页url
    last_text = soup.find('li', {'class': 'last'})
    last_text = last_text.find('a')
    last_url = main_url + last_text.get('href')

    i = 2
    while next_url != last_url:
        html = get_html(next_url)
        soup = get_soup(html)
        rank_list = get_rank_list(soup)
        writer_file(rank_list)
        next_url = get_next_url(soup)
        print('第{}页下载完成'.format(i))
        i += 1

    # 下载获取最后一页
    html = get_html(next_url)
    soup = get_soup(html)
    rank_list = get_rank_list(soup)
    writer_file(rank_list)
    print('第{}页下载完成'.format(i))


if __name__ == "__main__":
    main()
