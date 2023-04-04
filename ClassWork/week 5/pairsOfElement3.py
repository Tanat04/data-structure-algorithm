table_size = int(input())#5
A = list(map(int,input().split()))#[4,9,6,29,30]

hash_table = [[] for i in range(table_size)]

def hash_func(value): 
    return value % table_size

def insert(key, v):
    hash_index = hash_func(key)
    for each in hash_table[hash_index]:
        if key == each[0]:
            return -1
    hash_table[hash_index].insert(0,(key, v))
    return 0

def search(key):
    # return value of the key or
    # return -1 if s does not exists in hash table
    hash_index = hash_func(key)
    for each in hash_table[hash_index]:
        if each[0] == key:
            return each[1]
    return -1

def delete(key):
    # return 0 on successful deletion
    # return -1 if s does not exists in hash table
    hash_index = hash_func(key)
    if search(key) == -1:
        return -1
    else:
        for each in range(0,len(hash_table[hash_index])):
            if hash_table[hash_index][each][0] == key:
                del hash_table[hash_index][each]
                return 0

for i in range(table_size):
    keyI = A[i] + (i+1) * (i+1)
    result = search(keyI)
    if result == -1:
        insert(keyI, 1)
    else:
        delete(keyI)
        insert(keyI, result + 1)

#print(hash_table)

count = 0
for i in range(table_size):
    keyJ = A[i] - (i+1) * (i+1)
    value = search(keyJ)
    if value != -1:
        count += value

print(count)