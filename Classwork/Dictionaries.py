my_dict = {'key1':'value1','key2':'value2'}
#print(my_dict('key1')) can't do this although there is no syntax error
print(my_dict['key1'])


dict_one = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(dict_one['key2'][0])

dict_one['key1'] = dict_one['key1'] - 123
print(dict_one['key1'])

d={}
d['animal'] = 'Dog'
d['answer'] = 42
print(d)

x = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(x)
print(x['key1']['nestkey']['subnestkey'])
print(x['key1'])

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())