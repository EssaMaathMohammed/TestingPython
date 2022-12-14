from random import shuffle, randint

# the range operator provides [start, end, step] to our loop,
# it similar to a generator where we can cast it to a container like a list
# for num in range(3, 10, 2):
#     print(num)
#
# print(tuple(range(0,10)))

# the enumerate function is used to create
# a tuple of the iterable object that we are passing
# then we are going to use tuple unpacking to get the values
# the benefit of it is that we get the index we reached in a list easily
# letters = ['a', 'b', 'c', 'd', 'e']
# for index, letter in enumerate(letters):
#     print(index, letter)

# here we create a generator object that when
# iterated through will give us the result
# print(enumerate("a"))

# the zip function us used to merge its parameters into tuples
# print(list(zip([804, 3, 97, 348, 121], ['t', 'c', 'u', 'h', 'c'])))

# we use the in function to see whether an element exists in an iterable
# print('x' in 'kasdadwdszxca')

# min and max functions
# print(min([170, 254, 670, 797, 46]))
# print(max([70, 349, 170, 749, 354]))

# importing external libraries
# shuffle function from the random library is used to
# shuffle a list in place randomly
# shuffledList = [1, 2, 3, 4, 5, 6, 7, 8]
# shuffle(shuffledList)
# print(shuffledList)

# random function randint to generate a random integer
# print(randint(0, 10))

# to get the user input we use the input function
# this function always take the values in the state of
# strings, then we need to cast them using the int() float()
# functions
# num = input("enter you number")
# print(num)

# we can use the split function to split a string based on
# a regex
# a, b, c = input("enter three numbers").split()
# print(a, b, c)

# list comprehension we use a flattened out for loop to create
# a list
# mylist = [x for x in "word"]
# x = 0
# myList = [x for i in range(10)]
# if we want to put a condition to the assignment of the list
# myList = [x for x in range(20) if x % 2 == 0]

# the join method is used to join an iterable using the regex passed before the method
# print(" ".join(["hi", "hello"]))

# the abs function is used to get the abs value of the number passed
# print(abs(-100))
