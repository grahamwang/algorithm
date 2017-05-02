import time
begin_time = time.time()
find = {}  # find[node] = leader node of the connected component; in this case node is a tuple of binary bits
cluster = {}  # cluster[leader node of the connected component] = [node1, node2, node3,...]
size = {}  # size[leader node of the connected component] = size of the connected component
with open('clustering_big.txt', 'r') as fhand:
    for line in fhand:
        lst = tuple([int(s) for s in line.split()])
        if len(lst) == 2:
            n = lst[0]
            bit_size = lst[1]
        elif len(lst) > 2:
            find[lst] = find.get(lst, lst)
            cluster[lst] = cluster.get(lst, [lst])
            size[lst] = size.get(lst, 1)

# Generate indices for position of bit change
ind1 = [[s] for s in range(0, bit_size)]
ind2 = []
for i in ind1:
    for j in ind1:
        if i[0] != j[0]:
            ind2.append([i[0], j[0]])
ind1.extend(ind2)

def bit_change(t, ind):
    t = list(t)
    for i in ind:
        t[i] = abs(t[i] - 1)
    t = tuple(t)
    return t

for node in find:
    for ind in ind1:
        node_test = bit_change(node, ind)
        if node_test in find and find[node] != find[node_test]:
            larger_cluster, smaller_cluster = find[node], find[node_test]
            if size[smaller_cluster] > size[larger_cluster]:
                larger_cluster, smaller_cluster = smaller_cluster, larger_cluster
            # Update cluster size
            size[larger_cluster] += size[smaller_cluster]
            size.pop(smaller_cluster)
            # Update Union-Find
            for n in cluster[smaller_cluster]:
                find[n] = larger_cluster
            cluster[larger_cluster] += cluster[smaller_cluster]
            cluster.pop(smaller_cluster)

print(len(cluster))
print(time.time() - begin_time)
