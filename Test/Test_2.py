def upper_str(func):
    def inner():
        z = func()
        return z.upper()

    return inner

@upper_str
def enter_srting():
    return "good morning"

print(enter_srting())
