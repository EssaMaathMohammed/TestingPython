class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color


my_cat = Cat('sora', 'red')
print(my_cat.color, my_cat.name)


class Account:
    def __int__(self, owner, balance):
        raise NotImplementedError("Implement the owner balance constructor")

    def __str__(self):
        raise NotImplementedError("Implement the owner balance constructor")

    def withdraw(self):
        raise NotImplementedError("Implement the owner balance constructor")

