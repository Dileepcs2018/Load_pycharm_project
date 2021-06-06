num = 10
base = 1
bin = 0
while num > 0:
    rem = num%2
    bin  = bin + rem*base
    base = base*10
    num = num//2

print("bainaty",bin)



