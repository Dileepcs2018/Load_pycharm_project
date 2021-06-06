def smart_string(func):
    def inner():
        x = func()
        return x.upper()
    return inner


#@smart_string
def string_lower():
    return "this is good example"
print(string_lower())

a = smart_string(string_lower)

print(a())
