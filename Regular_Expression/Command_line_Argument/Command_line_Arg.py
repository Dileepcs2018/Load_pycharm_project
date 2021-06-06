import sys

print(sys.argv[0])
size = len(sys.argv)
sum = 0
for i in range(1,size):
    sum = sum + int(sys.argv[i])

print(sum)
