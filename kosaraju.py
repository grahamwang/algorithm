# Kosaraju's Two-Pass Algorithm to compute strong components in a directed graph
# The first Pass uses a depth-first search (DFS) loop starting from the highest labelled node
# to compute finishing time of each node
# The second Pass uses a depth-first search loop starting from the node with the highest finishing time
# to compute strongly connected components (SCC)

def SCC(G):
    # Construct a graph with all arcs reversed
    G_rev = dict()
    N_max = 0
    for u in G:
        if len(G[u]) > 0:
            for v in G[u]:
                G_rev[v] = G_rev.get(v, []) + [u]
                N_max = max(N_max, u, v)

    # If a node i has no outgoing edge, G_gev[i] = []
    for i in range(1, N_max + 1):
        G_rev[i] = G_rev.get(i, [])
    print(time.time() - time_begin)
    # Bookkeep whether a node has been explored in DFS
    explored = dict()
    for i in range(1, N_max + 1):
        explored[i] = 0

    # Initialize finishing time
    t = 0
    # Initialize a stack for DFS
    S = []
    # f is a dict to store finishing time, f[t] = u means node u's finishing time is t
    f = dict()
    # First pass
    for i in range(N_max, 0, -1):
        if explored[i] == 0:
            S.append(i)
            explored[i] = 1
            while len(S) > 0:
                N_to_exam = S[-1]
                N_out = G_rev[N_to_exam]
                if len(N_out) == 0:
                    # No outgoing edge, pop
                    t += 1
                    f[t] = S.pop()
                else:
                    N_out_unexplored = []
                    for v in N_out:
                        if explored[v] == 0:
                            N_out_unexplored.append(v)
                    if len(N_out_unexplored) == 0:
                        # No outgoing edge that has not been visited, pop
                        t += 1
                        f[t] = S.pop()
                    else:
                        # Find one unvisited outgoing edge, move on
                        S.append(N_out_unexplored[0])
                        explored[N_out_unexplored[0]] = 1
    print(time.time() - time_begin)
    S = []
    # Initialize leader list. leader[u] = [number of nodes visited during DFS started by node u]
    leader = dict()
    explored = dict()
    for i in range(1, N_max + 1):
        explored[i] = 0
    # Second pass
    for i in range(N_max, 0, -1):
        N_leader = f[i]
        if explored[N_leader] == 0:
            leader[N_leader] = 0
            S.append(N_leader)
            explored[N_leader] = 1
            while len(S) > 0:
                N_to_exam = S[-1]
                N_out = G[N_to_exam]
                if len(N_out) == 0:
                    leader[N_leader] += 1
                    S.pop()
                else:
                    N_out_unexplored = []
                    for v in N_out:
                        if explored[v] == 0:
                            N_out_unexplored.append(v)
                    if len(N_out_unexplored) == 0:
                        leader[N_leader] += 1
                        S.pop()
                    else:
                        S.append(N_out_unexplored[0])
                        explored[N_out_unexplored[0]] = 1
    print(time.time() - time_begin)
    SCC_sorted = sorted(leader.values(), reverse=True)
    # output the five largest SCCs
    return(SCC_sorted[0:5])

import time
time_begin = time.time()
G = dict()
# Read file, construct an adjacency list in which for node i, G[i] = [all nodes to which i has outgoing edges]
# Keep track of the maximum labeled node
N_max = 0
with open('SCC.txt', 'r') as fhand:
    for line in fhand:
        lst = [int(s) for s in line.split()]
        if len(lst) > 0:
            u = int(lst[0])
            v = int(lst[1])
            G[u] = G.get(u, []) + [v]
            N_max = max(N_max, u, v)

print(time.time()-time_begin)

# If a node i has no outgoing edge, G[i] = []
for i in range(1, N_max + 1):
    G[i] = G.get(i, [])

print(SCC(G))
print(time.time()-time_begin)
