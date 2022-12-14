def module_class_function():
    print("This is imported as a script Module")


if __name__ == '__main__':
    print(' this Module script is being run directly ')
    module_class_function()
else:
    print("Module imported!")
