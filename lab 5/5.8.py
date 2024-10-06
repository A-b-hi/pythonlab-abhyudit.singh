def convert_to_strings(lst, tpl):
    return list(map(str, lst + list(tpl)))

lst = [1, 2, 3]
tpl = (4, 5, 6)
print(convert_to_strings(lst, tpl))