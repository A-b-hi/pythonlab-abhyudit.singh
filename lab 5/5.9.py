def specific_tuple_elements(tup, index_list):
    return list(map(int, [tup[i] for i in index_list]))

tup = ('10', '20', '30', '40')
index_list = [1, 3]
print(specific_tuple_elements(tup, index_list)) 