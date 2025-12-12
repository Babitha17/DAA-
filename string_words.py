from collections import Counter

def sortByFrequency(arr):
    freq = Counter(arr)  
    sorted_items = sorted(freq.items(), key=lambda x: (x[1], x[0]))

    result = [item[0] for item in sorted_items]
    return result

arr = ["Ramesh", "Mahesh", "Mahesh", "Ramesh"]
output = sortByFrequency(arr)
print(output)

