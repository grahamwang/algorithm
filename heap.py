def heap_insert(H, key, max_or_min):
    # Insert key to heap H, depending on whether H supports extract-min or extract-max
    # H is an array representation of heap structure: children of i are 2i and 2i+1
    H.append(key)
    k = len(H)
    if max_or_min == 'min':
        while k // 2 - 1 >= 0 and H[k-1] < H[k//2-1]:
            H[k-1], H[k//2-1] = H[k//2-1], H[k-1]
            k = k // 2
    elif max_or_min == 'max':
        while k // 2 - 1 >= 0 and H[k-1] > H[k//2-1]:
            H[k-1], H[k//2-1] = H[k//2-1], H[k-1]
            k = k // 2
    else:
        print('Please specify ''min'' or ''max''')
    return H

def heap_extract(H, max_or_min):
    # Extract-min or -max from heap H, depending on whether H supports extract-min or extract-max
    H[0], H[-1] = H[-1], H[0]
    H.pop()
    n = len(H)
    k = 0
    if max_or_min == 'min':
        while 2*(k+1)+1 <= n and H[k] > min(H[2*(k+1)-1], H[2*(k+1)]):
            if min(H[2*(k+1)-1], H[2*(k+1)]) == H[2*(k+1)-1]:
                H[k], H[2*(k+1)-1] = H[2*(k+1)-1], H[k]
                k = 2*(k+1)-1
            else:
                H[k], H[2*(k+1)] = H[2*(k+1)], H[k]
                k = 2*(k+1)
    elif max_or_min == 'max':
        while 2*(k+1)+1 <= n and H[k] < max(H[2*(k+1)-1], H[2*(k+1)]):
            if max(H[2*(k+1)-1], H[2*(k+1)]) == H[2*(k+1)-1]:
                H[k], H[2*(k+1)-1] = H[2*(k+1)-1], H[k]
                k = 2*(k+1)-1
            else:
                H[k], H[2*(k+1)] = H[2*(k+1)], H[k]
                k = 2*(k+1)
    else:
        print('Please specify ''min'' or ''max''')
    return H

def median_maintenance_heap(L):
    # Given a sequence [x1...xn], at each time i, calculate the median of [x1...xi]
    # Use a low heap that support extract-max and a high heap that support extract-min
    M = []
    H_low = []
    H_high = []
    for i in range(0, len(L)):
        if i == 0:
            H_low.append(L[i])
            M.append(L[i])
        elif i == 1:
            H_high.append(L[i])
            if H_low[0] > H_high[0]:
                H_low[0], H_high[0] = H_high[0], H_low[0]
            M.append(H_low[0])
        else:
            if L[i] < H_high[0]:
                H_low = heap_insert(H_low, L[i], 'max')
            else:
                H_high = heap_insert(H_high, L[i], 'min')
            if len(H_low) - len(H_high) > 1:
                H_high = heap_insert(H_high, H_low[0], 'min')
                H_low = heap_extract(H_low, 'max')
            elif len(H_high) - len(H_low) > 1:
                H_low = heap_insert(H_low, H_high[0], 'max')
                H_high = heap_extract(H_high, 'min')
            if len(H_low) - len(H_high) in [0, 1]:
                M.append(H_low[0])
            elif len(H_low) - len(H_high) == -1:
                M.append(H_high[0])
    return M

# Example comparing running times. Heap is much faster
import time
L = list()
with open("Median.txt", "r") as fhand:
    for line in fhand:
        L.append(int(line.split()[0]))

# Use sorting
time_phase1 = time.time()
M = []
for i in range(0, len(L)):
    l = L[0:i+1]
    l.sort()
    if len(l) % 2 == 0:
        mid = l[len(l)/2 - 1]
    else:
        mid = l[(len(l)+1)/2 - 1]
    M.append(mid)
print(sum(M) % 10000)
print(time.time()-time_phase1)

# Use heap
time_phase2 = time.time()
M = median_maintenance_heap(L)
print(sum(M) % 10000)
print(time.time()-time_phase2)
