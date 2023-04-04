V,E = map(int, input().split())
edgeList = []

for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

#print(edgeList)

from mst_disjointsets import DisjointSets

s = DisjointSets(V)

edgeList.sort(key = lambda a:a[2])

#print(edgeList) #Sort by weight

W = 0
edgeCount = 0

for u,v,w in edgeList:
    if s.findset(u) != s.findset(v):
        W += w
        s.union(u,v)
        edgeCount += 1

if edgeCount == V-1:
    print("Connected")
    print(W)
else:
    print("Not Connected")

