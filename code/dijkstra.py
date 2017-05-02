# Implement Dijkstra's shortest path algorithm

def dijkstra(G, S):
    X = list()  # Initialize vertices processed so far
    X.append(S)
    A = dict()  # Initialize computed shortest path distances
    A[S] = 0
    B = dict()  # Initialize computed shortest paths
    B[S] = []
    V = G.keys()  # All vertices

    while len(X) <= len(V):
        shortest_distance = -1
        # Loop through all edges between X and V-X, find the shortest one, append w* to X
        # A[w*] = shortest distance of w*, B[w*] = shortest path
        for v in X:
            for w in G[v]:
                if w not in X:
                    if shortest_distance == -1:
                        shortest_distance = A[v] + G[v][w]
                        v_star = v
                        w_star = w
                    else:
                        if A[v] + G[v][w] < shortest_distance:
                            shortest_distance = A[v] + G[v][w]
                            v_star = v
                            w_star = w
        if shortest_distance == -1:
            break
        else:
            X.append(w_star)
            A[w_star] = A[v_star] + G[v_star][w_star]
            B[w_star] = B[v_star] + [w_star]

    # If there is no path from S to v, distance is set to be 1000000
    for v in V:
        A[v] = A.get(v, [1000000])
        B[v] = B.get(v, [])

    return A, B

# Example
G = dict()
# e.g G = {1: {2:10...}...} means vertex 1 has an outgoing edge to 2 with distance 10
with open("dijkstraData.txt", "r") as fhand:
    for line in fhand:
        lst = [int(s) for s in line.replace(',', ' ').split()]
        outgoing_edge = dict()
        for i in range(1, len(lst), 2):
            outgoing_edge[lst[i]] = lst[i+1]
            G[lst[0]] = outgoing_edge
A, B = dijkstra(G, 1)

