n = int(input())
inputAdj_List = [list(map(int, input().split())) for _ in range(n)]

color = ["WHITE"] * n
predecessor = [None] * n
d, f = [[-1] * n for _ in range(2)]
time = 0


def dfs_visit(adj_list, u):
    global time
    time += 1
    d[u] = time
    color[u] = "GREY"

    for i in range(adj_list[u][1]):
        v = adj_list[u][i+2]-1
        if color[v] == "WHITE":
            predecessor[v] = u
            dfs_visit(adj_list, v)

    color[u] = "BLACK"
    time += 1
    f[u] = time




def dfs(adj_list):
    for i in range(n):
        u = adj_list[i][0] - 1
        if color[u] == "WHITE":
            dfs_visit(adj_list, u)


dfs(inputAdj_List)
for v in range(n):
    print(*(v+1,d[v],f[v]))


