def listify_strings(strings):
    return list(map(list, strings))

strings = ['hello', 'world']
print(listify_strings(strings))