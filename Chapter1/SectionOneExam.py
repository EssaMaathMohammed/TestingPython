# d = {'k1': {'k2': 'hello'}} ----> print(d['k1']['k2'])
# d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]} print(d['k1'][0]['nest_key'][1][0])
# d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]} print(d['k1'][2]['k2'][1]['tough'][2][0])

# find the unique values of the following list
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(list5))

# build this list in two different ways [0,0,0]
# first way
l1 = [1, 2, 3] * 3
# second way
l2 = [0, 0, 0]

# there are two ways to sort a list
print(sorted([3, 2, 1]))  # gives a new list that is sorted
l3 = [3, 2, 1]
l3.sort()  # changes the original list
print(l1)
