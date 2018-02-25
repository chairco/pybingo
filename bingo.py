# -*- coding: utf-8 -*-
import random

n = 1  # 人數
success = 3  # bingo 數
split = 5
size = split * split  # 大小
#datas = dict(zip([chr(w) for w in range(97, 97 + n)],
#                 [random.sample(range(size), size) for i in range(0, n)]))  # 所有人畫的
datas = {'a': [10, 5, 24, 6, 18, 11, 3, 13, 7, 15, 12, 2, 16, 23, 21, 14, 20, 19, 17, 0, 9, 4, 22, 8, 1]}


def check_row(array, count=0):
    f = lambda a: map(lambda b: a[b:b + 5],
                      range(0, len(a) - 2, split))  # 建立 row 的 view
    for i in f(array):
        # fix bug(#10), remove sum(i) cause caculate 1
        if len([b for b in i if b is True]) == split:
            count += 1
        print(count, i)
    print('-'*10)
    return count


def check_column(array, split=split, count=0):
    board = []
    for i in range(split):
        row = [] * split
        board.append(row)

    for idx, num in enumerate(array):  # 建立 column 的 view
        if idx == 0:
            board[idx].append(num)
        else:
            i = idx % split
            board[i].append(num)

    for i in board:
        # fix bug(#10), remove sum(i) cause caculate 1
        if len([b for b in i if b is True]) == split:
            count += 1
        print(count, i)
    print('-'*10)

    return count


def caculate(data, count=0):
    for i in data:
        # fix bug(#10), remove sum(i) cause caculate 1
        if len([b for b in i if b is True]) == split:
            count += 1
        #print(count, i)
    #print('-'*10)
    return count


def bingo_search(num, data):
    for i in range(0, len(num)):
        data[data.index(num[i])] = True
        if i >= 12:  # start check, 5*5=13
            rol = check_row(data)
            col = check_column(data)
            if rol + col >= success:  # 計算成功數
                return i


if __name__ == '__main__':
    print(datas)  # 大家畫的

    result = dict()  # 計算每個人到第幾步贏 bingo
    num = [19, 23, 9, 7, 6, 10, 14, 8, 15, 2, 20, 18, 13, 4, 17, 21, 12, 0, 22, 1, 3, 11, 5, 16, 24] # 題目順序
    #num = random.sample(range(size), size)
    for k, v in datas.items():
        result.setdefault(k, bingo_search(num, data=v))

    print(result)  # 結果
    
    # not lambda
    order_result = {k: result[k]
                    for k in sorted(result, key=result.__getitem__)}
    print(order_result)
    
    # lambda
    order_result = {k: result[k]
                    for k in sorted(result, key=lambda x: result[x])}
    print(order_result)
