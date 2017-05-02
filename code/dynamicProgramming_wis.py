#  Dynamic programming to find the maximum weight independent set of a path graph
#  (a set of nodes that are not adjacent to each other, that has the largest sum of weights)

l = []
#  l is an array that starts with the total number of nodes
#  followed by weights of subsequent nodes in a path graph
with open('mwis.txt', 'r') as fhand:
    for line in fhand:
        if len(line.split()) > 0:
            l.append(int(line))

num_node = l[0]
node_weight = {}
for i in range(1, len(l)):
    node_weight[i] = l[i]

A = dict()
A[0] = 0
A[1] = node_weight[1]
for i in range(2, len(l)):
    A[i] = max(A[i-1], A[i-2]+node_weight[i])

independent_set = []
i = len(A) - 1
while i >= 1:
    if i == 1:
        independent_set.append(i)
        break
    if A[i-1] >= A[i-2] + node_weight[i]:
        i -= 1
    else:
        independent_set.append(i)
        i -= 2

test_set = [1, 2, 3, 4, 17, 117, 517, 997]
s = ""
for i in test_set:
    if i in independent_set:
        s += "1"
    else:
        s += "0"

print(s)
