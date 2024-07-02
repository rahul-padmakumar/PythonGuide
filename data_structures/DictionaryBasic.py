dict1 = {'key1': 'value1', 'key2': "value2", 'key3': 'value3'}
print(dict1)
print(dict1['key2'])
dict1['key3'] = 'value6'
dict1['key4'] = 'value4'
print(dict1)

# dictionary with multiple values

dict2 = {'key1': 1, 'key2': [1, 2, 3], 'key3': 2.50, 'key4': {'ikey1': 10, 'ikey2': 20}}
print(dict2)
print(dict2['key4']['ikey2'])

dict3 = {'a': 1, 'b': 2, 'c': 3}
dict3['b'] += 20
print(dict3)
dict3['b'] -= 10
print(dict3)

# dictionary functions
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.pop('key1'))
print(dict1)
dict1.clear()
print(dict1)