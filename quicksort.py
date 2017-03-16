# Compute the total number of comparisons used to sort the given input file by the QuickSort algorithm
# quick_sort_first() always uses the first element of the array as the pivot element
# quick_sort_last() always uses the final element of the array as the pivot element
# quick_sort_median() always uses the "median-of-three" pivot rule:
#     1) Consider the first, middle, and final elements. For an array with even length 2k, use the kth element as the middle element
#     2) Identify which of these three elements is the median and use it as the pivot
# Each function takes an array and output the number of comparisons and a sorted array

import numpy as np

def quick_sort_first(x):
    n = len(x)
    if n == 1: # Define the base case of the recursive call
        return n-1, x
    else:
        pivot = x[0] # Choose the first element as the pivot
        
        # Compare each element with the pivot
        # If it is smaller than the pivot, exchange it with the first element larger than the pivot
        # i represents the location of the first element larger than the pivot
        # The array becomes [pivot, all elements smaller, all elements larger]
        i = 1
        for j in range(1, n, 1):
            if x[j] < pivot:
                x[i], x[j] = x[j], x[i]
                i += 1
                
        # Exchange the pivot with the last element smaller than the pivot
        # The array becomes [all elements smaller, pivot, all elements larger]
        x[0], x[i - 1] = x[i - 1], x[0]
        
        # Recursive call
        # For each recursive call, the number of comparison is n-1
        if i == 1: # when all elements are larger than the pivot
            x_large = quick_sort_first(x[i:j+1])
            x = [x[i-1]] + x_large[1]
            count = n - 1 + x_large[0]
        elif i == n: # when all elements are smaller than the pivot
            x_small = quick_sort_first(x[0:i-2+1])
            x = x_small[1] + [x[i-1]]
            count = n - 1 + x_small[0]
        else:
            x_small = quick_sort_first(x[0:(i-2+1)])
            x_large = quick_sort_first(x[i:j+1])
            x = x_small[1] + [x[i-1]] + x_large[1]
            count = n - 1 + x_small[0] + x_large[0]
    return count, x

def quick_sort_last(x):
    n = len(x)
    if n == 1:
        return n-1, x
    else:
        # Exchange the pivot (final) element with the first element
        x[0], x[-1] = x[-1], x[0]
        pivot = x[0]
        
        i = 1
        for j in range(1, n, 1):
            if x[j] < pivot:
                x[i], x[j] = x[j], x[i]
                i += 1
        
        x[0], x[i-1] = x[i-1], x[0]
        
        if i == 1:
            x_large = quick_sort_last(x[i:j+1])
            x = [x[i-1]] + x_large[1]
            count = n - 1 + x_large[0]
        elif i == n:
            x_small = quick_sort_last(x[0:i-2+1])
            x = x_small[1] + [x[i-1]]
            count = n - 1 + x_small[0]
        else:
            x_small = quick_sort_last(x[0:(i-2+1)])
            x_large = quick_sort_last(x[i:j+1])
            x = x_small[1] + [x[i-1]] + x_large[1]
            count = n - 1 + x_small[0] + x_large[0]
    return count, x

def quick_sort_median(x):
    n = len(x)
    if n == 1:
        return n-1, x
    else:
        # Choose the pivot as the middle of the three and exchange it with the first element
        first = x[0]
        last = x[-1]
        mid = x[(n+1)/2-1]
        pivot = np.median([first, last, mid])
        if pivot == last:
            x[-1], x[0] = x[0], x[-1]
        elif pivot == mid:
            x[(n + 1) / 2 - 1], x[0] = x[0], x[(n + 1) / 2 - 1]
        
        i = 1
        for j in range(1, n, 1):
            if x[j] < pivot:
                x[i], x[j] = x[j], x[i]
                i += 1
        
        x[0], x[i - 1] = x[i - 1], x[0]
        
        if i == 1:
            x_large = quick_sort_median(x[i:j+1])
            x = [x[i-1]] + x_large[1]
            count = n - 1 + x_large[0]
        elif i == n:
            x_small = quick_sort_median(x[0:i-2+1])
            x = x_small[1] + [x[i-1]]
            count = n - 1 + x_small[0]
        else:
            x_small = quick_sort_median(x[0:(i-2+1)])
            x_large = quick_sort_median(x[i:j+1])
            x = x_small[1] + [x[i-1]] + x_large[1]
            count = n - 1 + x_small[0] + x_large[0]
    return count, x

# An example. It shows the "median-of-three" pivot rule has the best performance (least number of comparisons)
with open('QuickSort.txt', 'r') as fhand:
    text = fhand.readlines()
    int_list = [int(i) for i in text]
    
rlt1 = quick_sort_first(int_list[:])
rlt2 = quick_sort_last(int_list[:])
rlt3 = quick_sort_median(int_list[:])
print rlt1[0], rlt2[0], rlt3[0]


