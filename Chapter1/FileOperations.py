# to create a file
# %%writefile something.txt
# some random text
import os

# another way to create files is
with open("TestingFiles/myfile.txt", mode='w') as f:
    f.write("This is the second time im creating this file")

# to read files we need to set the mode to r
# for reading files we can either use readLines or read method
with open("TestingFiles/myfile.txt", mode='r') as f:
    resultOfReading = f.read()

print(resultOfReading + "\n")

# for appending text to files we use the "a" mode
with open("TestingFiles/myfile.txt", mode="a") as f:
    f.write("\nand this is the third time")

with open("TestingFiles/myfile.txt", mode='r') as f:
    resultOfReading = f.read()

print(resultOfReading)

# other modes for accessing files are r+, w+ for read write

# Write a script that opens a file named 'test.txt' , writes 'Hello World'  to the file, then closes it.
with open("test.txt", mode="w") as f:
    f.write("Hello World")

# if we only want to create a file we can use the x mode

f = open('something.txt', 'x')
if os.path.exists('C:\\Users\\study\\PycharmProjects\\TestingPython\\Chapter1\\TestingFiles\\theNewestFile.txt'):
    os.remove('C:\\Users\\study\\PycharmProjects\\TestingPython\\Chapter1\\TestingFiles\\theNewestFile.txt')
