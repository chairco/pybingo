# -*- coding: utf-8 -*-
import random

n = 5  # 人數
success = 3  # bingo 數
split = 5
size = split * split  # 大小
num = random.sample(range(size), size)  # 題目順序
datas = dict(zip([chr(w) for w in range(97, 97 + n)],
                 [random.sample(range(size), size) for i in range(0, n)]))  # 所有人畫的


def check_row(array, split=split):
    """return caculate graph row line's count
    :types: array: list
    :types: split: int
    :types: count: int
    :rtype: count: int
    """
    # print('checko_row')
    f = lambda a: map(lambda b: a[b:b + 5],
                      range(0, len(a) - 2, split))  # 建立 row 的 view
    count = caculate(data=f(array), split=split)
    return count


def check_column(array, split=split):
    """return caculate graph column line's count
    :types: array: list
    :types: split: int
    :types: count: int
    :rtype: count: int
    """
    # print('checko_column')
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
    count = caculate(data=board, split=split)
    return count


def check_hypotenuse(array, split=split):
    # print('checko_hypotenuse')
    f = lambda a: map(lambda b: a[b:b + 5],
                      range(0, len(a) - 2, split))  # 建立 hypotenuse 的 view
    h, h_reverse = [], []
    for idx, value in enumerate(f(array)):
        h.append(value[idx])
        h_reverse.append(value[::-1][idx])
    count = caculate(data=[h], split=split) + caculate(data=[h_reverse], split=split)
    return count


def caculate(data, split, count=0):
    """
    :types: data: list in list
    :types: split: int 
    :types: count: int
    """
    for idx, value in enumerate(data):
        # fix bug(#10), remove sum(i) cause caculate 1
        if len([b for b in value if b is True]) == split:
            count += 1
        #print(f"idx: {idx}, count: {count}, {value}")
    #print('-'*10)
    return count


def check_size(num, data, split=5):
    size = split * split
    if len(num) != size:
        raise ValueError(f"answer;s data {num} not equal {size}.")
    if len(data) != size:
        raise ValueError(f"user's data = {data}, not equal {size}.")
    return True


def check_success(split, success):
    if success > split * 2:
        raise ValueError(f'{success} more than the {split*2}')
    return True


def bingo_search(num, data, split, success):
    """search bingo
    :types: num: list
    :types: data: list
    :types: success: int
    :rtype: split: int
    """
    if check_size(num=num, data=data, split=split) and check_success(split=split, success=success):  # check data current and success
        for i in range(0, len(num)):
            if num[i] is 1:  # Fix bug, list.index(True) == list.index(1)
                idx = [idx for idx, value in enumerate(data) if value is 1]
                data[idx[0]] = True
            else:
                data[data.index(num[i])] = True
            if i >= split:  # (TODO) start check, min cross line
                rol = check_row(data)
                col = check_column(data)
                hyp = check_hypotenuse(data)
                if rol + col + hyp >= success:  # 加總成功數
                    return i + 1


def main(num=num, datas=datas, split=split, success=success, order=False):
    """main function
    :types: datas: dict: {user: value}
    :types: split: int: size of the graph
    :types: success: cross line
    :types: order: bool: order by value
    :rtype: order_result: dict
    """
    result = dict()  # 計算每個人到第幾步贏 bingo
    for k, v in datas.items():
        result.setdefault(k, bingo_search(
            num=num, data=v, split=split, success=success))
    if order:
        return result  # 結果
    else:
        # lambda
        # if not use lambda: order_result = {k: result[k] for k in
        # sorted(result, key=result.__getitem__)}
        order_result = {k: result[k]
                        for k in sorted(result, key=lambda x: result[x])}
        return order_result


if __name__ == '__main__':
    r = main()
    print(r)
