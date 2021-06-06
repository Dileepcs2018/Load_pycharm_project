#
def smart_div(func):
    def inner(x,y):
        if y ==0:
            print("InValid input")
            exit(0)
        return func(x,y)
    return inner(200,20)

@smart_div
def div(x,y):
    print(x//y)

#div(10,0)
