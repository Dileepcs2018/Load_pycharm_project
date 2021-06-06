import sys

print("Argument passed =",sys.argv[0])

size_of_args = len(sys.argv)

print("Number of arguments passed =",size_of_args)

print("Sum of number passed through arguments=")

sum = 0
for i in range(1,size_of_args):
    sum = sum + int(sys.argv[i])

print(sum)

