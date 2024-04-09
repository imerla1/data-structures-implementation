# we have 2 lists and we want to determine whether these two list have an item in common.
# lists are same size

def item_in_common_1(l1, l2):
    # Time complexity is o(n^2)
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False


def item_in_common_2(l1, l2):
    # usign hashmap
    # time Complexity is o(n)
    hash_map = dict()
    for i in l1:
        hash_map[i] = True
    for j in l2:
        if hash_map.get(j):
            return True
    return False

l1 = [1,2,3]
l2 = [3,2,1]