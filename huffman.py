def heap_insert(H, key, map_V, v):
    # Insert key(cheapest edge cost) to heap H. H supports extract-min
    # H is an array representation of heap structure: children of i are 2i and 2i+1
    # In the meanwhile update mapping to symbols
    H.append(key)
    map_V.append(v)
    k = len(H)
    while k//2-1 >= 0 and H[k-1] < H[k//2-1]:
        H[k-1], H[k//2-1] = H[k//2-1], H[k-1]
        map_V[k-1], map_V[k//2-1] = map_V[k//2-1], map_V[k-1]
        k //= 2
    return H, map_V

def heap_extract(H, map_V):
    # Extract-min from heap H and update mapping to symbols
    H[0], H[-1] = H[-1], H[0]
    map_V[0], map_V[-1] = map_V[-1], map_V[0]
    key = H.pop()
    v = map_V.pop()
    n = len(H)
    k = 0
    while 2*(k+1) <= n:
        if 2*(k+1)+1 > n:
            if H[k] > H[2*(k+1)-1]:
                H[k], H[2*(k+1)-1] = H[2*(k+1)-1], H[k]
                map_V[k], map_V[2 * (k + 1) - 1] = map_V[2 * (k + 1) - 1], map_V[k]
                k = 2*(k+1)-1
            else:
                break
        else:
            if H[k] > min(H[2*(k+1)-1], H[2*(k+1)]):
                if min(H[2*(k+1)-1], H[2*(k+1)]) == H[2*(k+1)-1]:
                    H[k], H[2*(k+1)-1] = H[2*(k+1)-1], H[k]
                    map_V[k], map_V[2 * (k + 1) - 1] = map_V[2 * (k + 1) - 1], map_V[k]
                    k = 2*(k+1)-1
                else:
                    H[k], H[2*(k+1)] = H[2*(k+1)], H[k]
                    map_V[k], map_V[2 * (k + 1)] = map_V[2 * (k + 1)], map_V[k]
                    k = 2*(k+1)
            else:
                break
    return H, map_V, key, v

def encode(l):
    #  l is an array that starts with the total number of symbols followed by weight of each symbol
    #  Implement Huffman algorithm to encode symbols in a way that minimizes the weighted average code length

    H = []  # heap of weights
    map_V = []  # mapping of symbols to weights in heap
    for i in range(1, len(l)):
        H, map_V = heap_insert(H, l[i], map_V, [i])

    enc = dict()  # initialize encoding of vertices. e.g. enc[i] = "1011"
    for i in map_V:
        enc[i[0]] = ""

    while len(map_V) >= 2:
        # Merge the two minimum weight symbols to form a new symbol
        # The weight of the new symbol is the sum of the two old symbols
        # Update encoding
        H, map_V, weight1, symbol1 = heap_extract(H, map_V)
        H, map_V, weight2, symbol2 = heap_extract(H, map_V)
        for v in symbol1:
            enc[v] = "0" + enc[v]
        for v in symbol2:
            enc[v] = "1" + enc[v]
        new_weight = weight1 + weight2
        symbol1.extend(symbol2)
        H, map_V = heap_insert(H, new_weight, map_V, symbol1)

    return enc


if __name__ == '__main__':
    l = []
    with open("huffman3.txt", "r") as fhand:
        for line in fhand:
            l.append(int(line))
    num_nodes = l[0]
    enc = encode(l)
    len_code = [len(s) for s in enc.values()]
    print(min(len_code))
    print(max(len_code))
    print(enc)
