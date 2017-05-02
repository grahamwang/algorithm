def heap_insert(H, key, map_V, v, map_E, e):
    # Insert key(cheapest edge cost) to heap H. H supports extract-min
    # H is an array representation of heap structure: children of i are 2i and 2i+1
    # In the meanwhile update mapping to vertices and edges
    H.append(key)
    map_V.append(v)
    map_E.append(e)
    k = len(H)
    while k//2-1 >= 0 and H[k-1] < H[k//2-1]:
        H[k-1], H[k//2-1] = H[k//2-1], H[k-1]
        map_V[k-1], map_V[k//2-1] = map_V[k//2-1], map_V[k-1]
        map_E[k-1], map_E[k//2-1] = map_E[k//2-1], map_E[k-1]
        k //= 2
    return H, map_V, map_E

def heap_delete(H, v, map_V, map_E):
    # Delete vertex (cheapest edge cost of the vertex) in position k from heap H
    # Update mapping to vertices and edges
    k = map_V.index(v)
    H[k], H[-1] = H[-1], H[k]
    map_V[k], map_V[-1] = map_V[-1], map_V[k]
    map_E[k], map_E[-1] = map_E[-1], map_E[k]
    H.pop()
    map_V.pop()
    map_E.pop()
    n = len(H)
    if k == n:
        return H, map_V, map_E
    else:
        while 2 * (k + 1) <= n:  # bubble down if larger than child
            if 2 * (k + 1) + 1 > n:
                if H[k] > H[2 * (k + 1) - 1]:
                    H[k], H[2 * (k + 1) - 1] = H[2 * (k + 1) - 1], H[k]
                    map_V[k], map_V[2 * (k + 1) - 1] = map_V[2 * (k + 1) - 1], map_V[k]
                    map_E[k], map_E[2 * (k + 1) - 1] = map_E[2 * (k + 1) - 1], map_E[k]
                    k = 2 * (k + 1) - 1
                else:
                    break
            else:
                if H[k] > min(H[2 * (k + 1) - 1], H[2 * (k + 1)]):
                    if min(H[2 * (k + 1) - 1], H[2 * (k + 1)]) == H[2 * (k + 1) - 1]:
                        H[k], H[2 * (k + 1) - 1] = H[2 * (k + 1) - 1], H[k]
                        map_V[k], map_V[2 * (k + 1) - 1] = map_V[2 * (k + 1) - 1], map_V[k]
                        map_E[k], map_E[2 * (k + 1) - 1] = map_E[2 * (k + 1) - 1], map_E[k]
                        k = 2 * (k + 1) - 1
                    elif min(H[2 * (k + 1) - 1], H[2 * (k + 1)]) == H[2 * (k + 1)]:
                        H[k], H[2 * (k + 1)] = H[2 * (k + 1)], H[k]
                        map_V[k], map_V[2 * (k + 1)] = map_V[2 * (k + 1)], map_V[k]
                        map_E[k], map_E[2 * (k + 1)] = map_E[2 * (k + 1)], map_E[k]
                        k = 2 * (k + 1)
                else:
                    break
        while (k + 1) // 2 - 1 >= 0 and H[k] < H[(k + 1) // 2 - 1]:  # bubble up if smaller than parent
            H[k], H[(k + 1) // 2 - 1] = H[(k + 1) // 2 - 1], H[k]
            map_V[k], map_V[(k + 1) // 2 - 1] = map_V[(k + 1) // 2 - 1], map_V[k]
            map_E[k], map_E[(k + 1) // 2 - 1] = map_E[(k + 1) // 2 - 1], map_E[k]
            k = (k + 1) // 2 - 1
        return H, map_V, map_E

def minimum_span_tree(G):
    # Calculate the minimum span tree of a connected undirected graph G using Prim's algorithm (eager implementation)
    V = G.keys()
    X = [V[0]]  # vertices added to the minimum span tree
    H = []  # heap array of cheapest edge cost of every node in V-X to X; inf if no such edge exists
    map_V = []  # mapping of vertices to H; contains all nodes in V-X
    map_E = []  # mapping of edges to H and map_V; contains cheapest edge of every node in V-X to X; None if no such edge exists
    MST = dict()  # minimum span tree (MST): MST[edge] = edge cost

    # Initialize heap with O(m log(n)) pre-processing
    for v in V:
        if v in X:
            continue
        edge_cost = float('inf')
        edge = None
        for e in G[v]:
            if e[0] in X and e[1] < edge_cost:
                edge_cost = e[1]
                edge = (e[0], v)
        H, map_V, map_E = heap_insert(H, edge_cost, map_V, v, map_E, edge)

    while len(X) < len(V):
        # Update X and MST
        v = map_V[0]  # vertex added to X
        if H[0] == float('inf'):
            print("MST does not exists: graph is not connected")
            break
        X.append(v)
        MST[map_E[0]] = H[0]  # edge and edge cost added to MST
        # Extract min from H, update map_V and map_E
        H, map_V, map_E = heap_delete(H, v, map_V, map_E)
        # For each edge (v, w), if w is not in X and the current cheapest edge of w to X is larger than (v, w),
        # delete edge cost of w from heap H, recompute edge cost of w, and reinsert into heap
        for e in G[v]:
            if e[0] not in X and e[1] < H[map_V.index(e[0])]:
                H, map_V, map_E = heap_delete(H, e[0], map_V, map_E)
                H, map_V, map_E = heap_insert(H, e[1], map_V, e[0], map_E, (v, e[0]))
    return MST

if __name__ == '__main__':
    G = dict()
    with open('edges2.txt', 'r') as fhand:
        for line in fhand:
            lst = [int(s) for s in line.split()]
            if len(lst) == 2:
                n = lst[0]  # number of vertices
                m = lst[1]  # number of edges
            elif len(lst) > 2:
                G[lst[0]] = G.get(lst[0], []) + [lst[1:]]
                G[lst[1]] = G.get(lst[1], []) + [[lst[0], lst[2]]]

    MST = minimum_span_tree(G)
    print(sum(MST.values()))
