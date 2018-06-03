# Sort list by freq and increasing order
import collections
lst = [1,2,3,4,3,3,3,6,7,1,1,9,3,2]
counts = collections.Counter(lst)
new_list = sorted(lst, key=lambda x: -counts[x])
print(new_list)
