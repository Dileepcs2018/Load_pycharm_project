def smart_div(func):
    def inner(x,y):
        if y == 0:
            return "please provide valid input"
        return func(x,y)
    return inner

@smart_div
def div(a,b):
    return a//b

z = div(4,2)
print(z)