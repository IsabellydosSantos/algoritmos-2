def func(p):
    global a
    a = b + 30
    print("res = ", p + a)


a = 10
func(a)
b = 20
