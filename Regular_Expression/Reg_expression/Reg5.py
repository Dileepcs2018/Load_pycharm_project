import re
f1 = open('input','r')
f2 = open('output.txt','w')

for line in f1:
    #print(line)
    list1 = re.findall('[6-9]\d{9}',line)
    for number in list1:
        f2.write(number+'\n')
        print()
    print()

f1.close()
f2.close()