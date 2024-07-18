def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = [1, 'STRING', True]
values_dict = {'a': 1, 'b': False, 'c': 'sss'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [23.23, 'value']
print_params(*values_list_2, 42)

