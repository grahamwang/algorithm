G = dict()
with open('edges.txt', 'r') as fhand:
    for line in fhand:
        lst = [int(s) for s in line.split()]
        if len(lst) == 2:
            n = lst[0]
            m = lst[1]
        elif len(lst) > 2:
            G[(lst[0], lst[1])] = lst[2]

V = []
for key in G.keys():
    for s in key:
        if s not in V:
            V.append(s)

X = [1]
T = dict()

while len(X) <= len(V):
    min_edge_cost = float("inf")
    for key in G.keys():
        if (key[0] in X) != (key[1] in X):
            if G[key] < min_edge_cost:
                min_edge_cost = G[key]
                min_edge = key
    T[min_edge] = G[min_edge]
    for v in min_edge:
        if v not in X:
            X.append(v)
    if len(X) == len(V):
        break

print(sum(T.values()))








