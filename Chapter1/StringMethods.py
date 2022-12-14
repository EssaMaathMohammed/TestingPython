x = "hello world"
print(x)

print(x[3])

# last letter of string
print(x[-1])

# string slicing
print(x[:4])
# reverse a string [start:stop:steps]
print(x[::-1])
# length of string
print(len(x))
# concatenation operations
x = x + x
print(x)
x = x * 2
print(x)
# split based on a regex
print(x.split("hello"))

# string interpolation
print("this is my age: {a} and this is my name: {n}".format(a="21", n="essa"))
age = 21
name = 'essa'
print(f"this is my age {age} and this is my name {name}")