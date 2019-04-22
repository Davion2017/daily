import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url)
    response.encoding='utf-8'
    html = response.text
    # print(response)
    return html


def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup


def get_rank_list(soup):
    rank_text_list = soup.find("table", {"class": "results table table-condensed"})
    rank_text_list = rank_text_list.find_all('tr')[4:]
    rank_list = []
    for rank_text in rank_text_list:
        rank = rank_text.find("td", {"class": "r"}).extract().text
        name = rank_text.find("a", {"class": "p"}).extract().text
        score = rank_text.find("td", {"class": "R2"}).extract().text
        if rank == '\xa0':
            rank = None
        item = (rank, name, score)
        rank_list.append(item)
    return rank_list


def writer_file(rank_list):
    header = ('Rank', 'Name', 'Result')
    with open('333_single_China_top100.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for rank in rank_list:
            writer.writerow(rank)


def main():
    start_url = 'https://www.worldcubeassociation.org/results/events.php?regionId=China'
    # start_url = 'https://cubingchina.com/results/rankings'
    html = get_html(start_url)
    # print(html)
    soup = get_soup(html)
    rank_list = get_rank_list(soup)
    writer_file(rank_list)
    for rank in rank_list:
        print(rank)


if __name__=="__main__":
    main()