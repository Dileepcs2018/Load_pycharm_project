
file = open('file',"r")

for line in file:
    li = line.strip()
    if not li.startswith("#"):
        print(li.rstrip())
