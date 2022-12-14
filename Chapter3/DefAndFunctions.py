# def sum_two_numbers(num1, num2):
#     return num1 + num2
#
#
# def even_numbers_in_list(check_list):
#     """ returns even numbers in a list """
#     even_list = []
#     for item in check_list:
#         if item % 2 == 0:
#             even_list.append(item)
#     return even_list
#
#
# def check_best_employee(employees_to_check):
#     max_hours = 0
#     best_employee = ""
#     for name, hours in employees_to_check:
#         if hours > max_hours:
#             max_hours = hours
#             best_employee = name
#     return best_employee, max_hours


# check who worked the max amount of hours
# employees = [('essa', 220), ('nada', 500), ('zanyar', 230)]
# name, hours = check_best_employee(employees)
# print(name, hours)

# *args and **kwargs
# args passes a list (numbers), kwargs as a dictionary (word=value)
# def sum_the_following(*args, **kwargs):
#     print(sum(args))
#     print(sum(kwargs.values()))
# sum_the_following(1, 2, 3, 4, 5, one=1, two=2, three=3)

# upper if index is even otherwise lower
# def myfunc(word):
#     final_word = ""
#     for index, letter in enumerate(word):
#         if index % 2 == 0:
#             final_word += letter.upper()
#         else:
#             final_word += letter.lower()
#     return final_word
