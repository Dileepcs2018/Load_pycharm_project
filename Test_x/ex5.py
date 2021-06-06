file = open("python_text")
line = file.read()

new_line = line.strip()
for l in new_line:
    #print(l,l,end="")
    if not l.startswith('#'):
         print(l,end="")






