# lists
# they can be appended and popped
# they can be of multiple data types
# they are mutable strings
# we can use the sort and reverse methods and change the original list
numbers = [1, 2, 3.14]
print(numbers[1:])
numbers.append(5)
lastElement = numbers.pop()
print(lastElement)
# we cannot print the result of numbers.sort because the method returns None
numbers.sort()
len(numbers)
print(numbers)

# dictionaries
# key-value paris, where we can get the keys and values using
# dic.keys(), dic.values()
# they are also mutable
numbers = {'key1': 1, 'key2': 2, 'key3': 3}
print(numbers.keys())
print(numbers.values())

# Tuples
# the only difference between the list and tuples is immutability
# they only have two methods, count for counting how many times the value got dupl
# index to return the first occurrence index of a value
numbers = (1, 4, 6)
numbers.count(4)
print(numbers.index(4))

# Sets
# Sets doesn't allow duplicates and are unordered, we can cast other types
# of lists to sets, and it will remove all the duplicate values
# we can add using the add method, and remove using the remove method
numbers = set()
numbers.add(6)
print(numbers)
testList = [1, 2, 2, 2, 2, 2, 3, 3, 3, 34, 4]
numbers = set(testList)
print(numbers)
# we can add iterable objects inside sets, and it will convert them to unique values only
set1 = set("Mississippi")
print(set1)
