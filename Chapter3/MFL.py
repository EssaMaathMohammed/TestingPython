# maps are used when we want to point a value to something else
# we can map functions into iterables to make those functions execute
# with the iterable elements
# def add_the_letter(word):
#     for letter in word:
#         print(letter + "O")
#
#
# words = "hellothere"
# list(map(add_the_letter, words))
#

# filter is used decides to allow or deny the element
# based on a bool value, the usage is almost the same as map

# def even_or_odd(num):
#     return num % 2 == 0

# numList = [209, 398, 718, 608, 717]
# myEvenList = list(filter(even_or_odd, numList))

# if we intend to use a function once and not let it take
# space we can use a lambda function
# numList = [209, 398, 718, 608, 717]
# list(filter(lambda num: num % 2 == 0, numList))

# get the first letter from each string
# letterList = " ".join(map((lambda word: word[0]), ['ze', 'ee', 'xe', 'ye', 'ke']))
