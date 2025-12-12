def findMedian(arr):
    arr.sort()               
    n = len(arr)
    mid = n // 2             
    return arr[mid]          


