import queue


adj = [(0,-1), (0,1), (-1,0), (1,0)] # All the steps we can make

def valid(r, c): # Check if the moves are valid
    # Return True if the coordinate is not outside matrix
    # and is not a part of the wall
    
    global steps

    if r >= 0 and r < 10 and c >=0 and c < 10:
        if steps[r][c] == 0:
            return True
    return False

maze = [] # For input matrix
pos = [] # For starting and ending point

for i in range(10):
    maze.append(input())
print("This is input(maze): \n", maze)

steps = [[0]*10 for i in range(10)] # Creating a list of 10x10 with all elements = 0
print("\nSteps: \n", steps)

for r in range(10):
    for c in range(10):
        if maze[r][c] == '#':
            steps[r][c] = -1
        if maze[r][c] == 'X':
            pos.append((r,c))
# check which index in 'maze' list is '#', change that index in steps list to '-1'(Wall)
# Locate the starting and ending point('X') then append the index as tuple to 'pos' list 

print("\nUpdate steps and pos:")
print("Steps: \n", steps)
print("\npos: \n", pos)

Queue = []
Queue.append((pos[0], 0))
print("\nQueue: ", Queue, "\n")

while Queue != []:
    u = Queue[0] #((6,1),0) 
    del Queue[0] #[]

    if u[0] == pos[1]:
        print(u[1])
        break

    for d in adj:
        r = u[0][0] + d[0]#X, 6
        c = u[0][1] + d[1]#Y, -1
        #print("r and c: ", (r, c) )#(6, 1)

        if valid(r, c):
            v = ((r,c), u[1]+1)
            steps[r][c] = u[1] + 1
            Queue.append(v)
        #print("Steps: ", steps)
        #print("Queue: ", Queue, "\n")        
