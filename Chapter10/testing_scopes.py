s = 'global'


def func_with_local_vars():
    b = 'local var'
    print('local vars inside the func_with_local_vars function are\n', locals())


print('all of these are global vars:\n', globals().keys())
func_with_local_vars()
