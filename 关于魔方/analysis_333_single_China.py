'''
    功能：根据成绩生成直方图，分析中国选手成绩分布图
    作者：Davion
    版本：V1.0
    日期：2018/03/13
'''

import csv
import matplotlib.pyplot as plt


# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False


def get_date(file):
    date = []
    with open(file, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for item in reader:
            try:
                date.append(float(item[2]))
            except:
                pass
    return date


def view(date):
    tick_labels = []
    for i in range(3, 61):
        tick_labels.append(str(i))
    plt.hist(date, bins=range(3, 61), edgecolor='black', linewidth=1)

    plt.xticks(range(3, 61), tick_labels)
    plt.title('Ditribution')
    plt.xlabel('Second')
    plt.ylabel('Count')
    plt.show()


def main():
    file = '333_single_China.csv'
    date = get_date(file)
    view(date)


if __name__ == '__main__':
    main()
