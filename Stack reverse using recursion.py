def reverse_queue(arr):
    if len(arr) == 0:
        return
    temp= arr.pop()
    reverse_queue(arr)
    arr.insert(0,temp)
    return arr

print(reverse_queue([1,2,3,4,5]))
