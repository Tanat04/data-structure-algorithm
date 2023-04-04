test_cases = int(input())

count = 0
mod = 101
num = 19

hash_table = [0 for i in range(mod)]

def hash(key): 
    ans = 0
    for i in range(len(key)):
        ans += ord(key[i]) * (i+1)
    return (num * ans) % mod

def nextPos(key, j):
    return (hash(key) + (j * j) + (23 * j)) % mod

def insert(key):
    global count
    for i in range(0, num+1):
        if hash_table[nextPos(key, i)] == 0 or hash_table[nextPos(key, i)] == "empty":
            hash_table[nextPos(key, i)] = key
            count += 1
            return True
    return False

def exist(key):
    for i in range(0, num):
        if hash_table[nextPos(key, i)] == key:
            return True
    return False

def delete(key):
    global count
    for i in range(0, num):
        if hash_table[nextPos(key, i)] == key:
            hash_table[nextPos(key, i)] = "empty"
            count -= 1
            return True
    return False

def reset():
    global count
    for i in range(mod):
        hash_table[i] = 0
    count = 0

for i in range(test_cases):
    reset()
    n = int(input())
    for i in range(n):
        s = input()
        strs = s.split(":")
        if strs[0] == "ADD" and exist(strs[1]) == False:
            insert(strs[1])
        elif strs[0] == "DEL" and exist(strs[1]) == True:
            delete(strs[1])

    print(count)
    for i in range(mod):
        if hash_table[i] != 0 and hash_table[i] != "empty":
            print(f"{i}:{hash_table[i]}")
    print()
#print(hash_table)
