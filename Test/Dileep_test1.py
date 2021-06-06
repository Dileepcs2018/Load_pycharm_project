import argparse

parse = argparse.ArgumentParser()
parse.add_argument("--num1", help= "enter num1")
parse.add_argument("--num2", help="enter num2")
parse.add_argument("--operation",help = "enter operation")

args = parse.parse_args()

n1 = args.num1
n2 = args.num2
r = 0

if args.operation == "add":
    r  = n1 +n2
    print(r)