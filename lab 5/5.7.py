def add_and_difference(l1, l2):
    addition = list(map(lambda x, y: x + y, l1, l2))
    difference = list(map(lambda x, y: x - y, l1, l2))
    return addition, difference

l1 = [10, 20, 30,80,31]
l2 = [1, 2, 3,78,12]
print(add_and_difference(l1, l2))  