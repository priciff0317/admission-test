# Q1
def find_max(numbers):
    max_num = 0
    for i in numbers:
        if i > max_num:
            max_num = i
    return max_num

def find_positions(numbers, target):
    i = 0
    while i < len(numbers):
        if target == numbers[i]:
            return i
        else:
            i+=1
    else:
        return -1

print(find_max([1,2,4,5]))
print(find_max([5,2,7,1,6]))

print(find_positions([5,2,7,1,6],5))
print(find_positions([5,2,7,1,6],7))
print(find_positions([5,2,7,7,7,1,6],7))
print(find_positions([5,2,7,1,6],8))

# Q2

def count(input):
    d = {}
    for i in range(len(input)):
        if input[i] not in d:
            d[input[i]] = 1
        else:
            d[input[i]] += 1
    return d

input1 = ['a','b','c','a','c','a','x']
print(count(input1))

def group_by_key(numbers):
    d = {}

    for i in numbers:
        v = i['value']
        k = i['key']
        if k not in d:
            d[k] = v
        else:
            d[k] += v
    return d

input2 = [
    {'key':'a', 'value':3},
    {'key':'b', 'value':1},
    {'key':'c', 'value':2},
    {'key':'a', 'value':3},
    {'key':'c', 'value':5},
          ]
print(group_by_key(input2))

# Q3

# 1. what is git and why is used ?
# git 是版本流程控制，主要是將變動的資料進行每個版本的歷史追蹤與更改並且確保項目的完整性和可追溯性。
# git 也可以用於管理任何類型的文本文件，而不只是代碼文件。

# 2. what is the difference between list, dictionary, tuple, set in python?

# list 是有序且可變動資料的資料結構，可以儲存不同的資料類型
# dictionary 是無序且可變動的資料結構，每個key對應一個value
# tuple 是有序且不可變動的資料結構，可以儲存不同的資料類型
# set 是無序可變動的資料結構








