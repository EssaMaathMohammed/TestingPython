def public_fun(secure_call):
    print("outside")
    secure_call()
    print("outside")


@public_fun
def secure_function():
    print("hello you are calling me internally")


