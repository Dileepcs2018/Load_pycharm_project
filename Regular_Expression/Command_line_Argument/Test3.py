# Python program to demonstrate
# command line arguments

import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")

# Addition of numbers Using
# argparse
# module
Sum = 0
for i in range(1, n):
    Sum += int(sys.argv[i])

print("\n\nResult:", Sum)
print(sys.argv)


s  = "abc"

# x = isinstance(5, int)
# print(x)
for i in s:
    if isinstance(i,int):
        print("it is interger")

    else:
        print("it is string")