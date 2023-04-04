import random as rd

def no_switch():
    Choice = ["A","B","C"]
    goat = Choice.copy()

    prize = rd.choice(Choice)
    goat.remove(prize)


    selection = rd.choice(Choice)
    return prize == selection

def switch():
    Choice = ["A", "B", "C"]
    goat = ["A", "B", "C"]

    prize = rd.choice(Choice)
    goat.remove(prize)

    selection = rd.choice(Choice)
    if selection == goat[0]:
        Choice.remove(goat[1])
    else:
        Choice.remove(goat[0])
    Choice.remove(selection)


    return prize == Choice[0]

n = 100000
noswt = 0
swt = 0

for i in range(n):
    if no_switch():
        noswt += 1
    if switch():
        swt += 1


print(f"""No Switch Winning Chance: {(noswt / n) * 100} %
Switch Winning Chance: {(swt / n) * 100} %""")
