# we cause a type error and handle it in the
# except block (catch)
try:
    # result = 5 + '5'
    result = 5 + '5'
except TypeError:
    print("you entered a variable that is not a number")
else:
    print(f"there was no error you result is: {result}")
finally:
    print("i always run")
