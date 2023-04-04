
class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0]*n

    def findset(self, u):
        if self.p[u] == u:
            return u 
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u, v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

# djs = DisjointSets(5)

# for i in range(5):
#     print(djs.findset(i), djs.p, djs.rank)

# print()
# djs.union(3,4)
# print(djs.findset(3), djs.p, djs.rank)
# print(djs.findset(4), djs.p, djs.rank)

# print()
# djs.union(1,2)
# print(djs.findset(1), djs.p, djs.rank)
# print(djs.findset(2), djs.p, djs.rank)

# print()
# for i in range(5):
#     print(djs.findset(i))

# print()
# djs.union(1,4)
# for i in range(5):
#     print(djs.findset(i), djs.p, djs.rank)