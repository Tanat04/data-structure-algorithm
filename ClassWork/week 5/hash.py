from sys import stdin

operations = []
for line in stdin:
    line = line.split()
    if len(line) > 2:
        line[2] = int(line[2])
    operations.append(line) 

table_size = 12    # set table size here
hash_table = [[] for i in range(table_size)]

def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')

def hash_func(roman):
    value = 0
    for chr in roman:
        value += ord(chr)
    return value % table_size

def insert(roman, v):
    hash_index = hash_func(roman)
    for each in hash_table[hash_index]:
        if roman == each[0]:
            return -1
    hash_table[hash_index].insert(0,(roman, v))
    return 0

def search(roman):
    # return value of the key or
    # return -1 if s does not exists in hash table
    hash_index = hash_func(roman)
    for each in hash_table[hash_index]:
        if each[0] == roman:
            return each[1]
    return -1

def delete(roman):
    # return 0 on successful deletion
    # return -1 if s does not exists in hash table
    hash_index = hash_func(roman)
    if search(roman) == -1:
        return -1
    else:
        for each in range(0,len(hash_table[hash_index])):
            if hash_table[hash_index][each][0] == roman:
                del hash_table[hash_index][each]
                return 0

for op in operations:
    if op[0] == "insert":
        insert(op[1],op[2])
        show_hash_table()
    elif op[0] == "delete":
        delete(op[1])
        show_hash_table()
    elif op[0] == "search":
        print(search(op[1]))
    else:
        print("fuck u")