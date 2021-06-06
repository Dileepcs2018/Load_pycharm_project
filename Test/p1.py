import sys

size = len(sys.argv)

print("\nName of Python script:", sys.argv[0])

sum = 0

for i in range(1,size):
    sum = sum + int(sys.argv[i])

print(sum)