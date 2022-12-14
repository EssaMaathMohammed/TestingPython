# create a for loop and iterate through a list
# numberList = [1, 2, 3]
# for num in numberList:
#     print(num)

# iterating through a string
# for letter in "this string":
#     print(letter)

# when we don't intent to use the placeholder
# we replace it with _
# for _ in "hello":
#     print("cool")

# Tuple Unpacking is where we copy the structure of the
# object and use it in a loop or any other matter
# this will print each item in the list which is a tuple
# myList = [(1, 2), (3, 4), (5, 6), (7, 8)]
# for item in myList:
#     print(item)

# if we want access to each item in each tuple we can
# copy the structure of the tuple inside the placeholder
# for (num1, num2) in myList:
#     print(num1, num2)

# we can do that as-well in each
# object that has a representable structure
# l1 = [1, 2, 4]
# l2 = [2, 3, 4]
# l3 = [3, 4, 4]
# myNestedList = [l1, l2, l3]
# for (num1, num2, num3) in myNestedList:
#     print(num1, num2, num3)

# for iterating in objects we can use the items method
# to get a tuple like structure then we can use tuple unpacking with it
# for key, value in {'k1': 1, 'k2': 2, 'k3': 3}.values():
#     print(key, value)


# while loop
# x = 1
# while x < 10:
#     x += 1
# else:
#     print(f"{x} is more than 10")

# myList = [word[0] for word in 'hello world'.split()]

