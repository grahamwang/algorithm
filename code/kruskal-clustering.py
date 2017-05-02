edge = {}  # edge[edge cost] = [(node1, node2), (node3, node4),...]
find = {}  # find[node] = leader node of the connected component
cluster = {}  # cluster[leader node of the connected component] = [node1, node2, node3,...]
size = {}  # size[leader node of the connected component] = size of the connected component
with open('clustering1.txt', 'r') as fhand:
    for line in fhand:
        lst = [int(s) for s in line.split()]
        if len(lst) == 1:
            n = lst[0]  # Number of nodes
        elif len(lst) == 3:
            edge[lst[2]] = edge.get(lst[2], []) + [(lst[0], lst[1])]
            find[lst[0]] = find.get(lst[0], lst[0])
            find[lst[1]] = find.get(lst[1], lst[1])
            cluster[lst[0]] = cluster.get(lst[0], [lst[0]])
            cluster[lst[1]] = cluster.get(lst[1], [lst[1]])
            size[lst[0]] = size.get(lst[0], 1)
            size[lst[1]] = size.get(lst[1], 1)

edge_cost_sorted = sorted(edge.keys())
k = len(cluster)
i = 0
for edge_cost in edge_cost_sorted:  # Iterate from the smallest edge cost
    for j in edge[edge_cost]:  # Iterate over all edges with cost i
        if find[j[0]] != find[j[1]]:  # Check if two nodes in the edge are from the same cluster/component
            larger_cluster, smaller_cluster = find[j[0]], find[j[1]]
            if size[smaller_cluster] > size[larger_cluster]:
                larger_cluster, smaller_cluster = smaller_cluster, larger_cluster
            # Update cluster size
            size[larger_cluster] += size[smaller_cluster]
            size.pop(smaller_cluster)
            # Update Union-Find
            for node in cluster[smaller_cluster]:
                find[node] = larger_cluster
            cluster[larger_cluster] += cluster[smaller_cluster]
            cluster.pop(smaller_cluster)
            k -= 1
        if k == 3:
            break
    else:
        i += 1
        continue
    break

print(edge_cost_sorted[i])
