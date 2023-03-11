# intersection
# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.

# test_00:
# intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
# test_01:
# intersection([2,4,6], [4,2]) # -> [2,4]
# test_02:
# intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]



from collections import Counter
def intersection(a, b):
    count_b = Counter(b)
    duplicate_ele = []
    for num in a:
      if num in count_b:
        duplicate_ele.append(num)
    return duplicate_ele

def intersection(a, b):
    set_a = set(a)
    set_b = set(b)
    return [ x for x in set_a if x in set_b]
    