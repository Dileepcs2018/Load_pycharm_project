x = open("file","r")

for line in x:
    li = line.strip()
    if not li.startswith('#'):
        print(li)