# def even_number_until(amount):
#     for num in range(1, amount):
#         yield num * 2
#
#
# print([x for x in even_number_until(20)])

# make the letters into a generator, using the iter func, then get the next value using the next func
letters = iter('okoadkawokdakdowdzvcpkpq')
count = 0
for letter in letters:
    print(letter)
    count += 1
    if count == 10:
        break

# when iterating over a generator, if we stop during the
# interation the value we reached will be the next value to get,
# this means next is being called internally
# if we don't make the letters into a generator all the for loop will do is
# to iterate over the indexes
print(next(letters))


