import re

file = open("file","r")

lines = file.read()
print(lines)

n = lines.count("10.2.0.24")
print(n)