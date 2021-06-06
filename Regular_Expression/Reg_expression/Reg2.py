import re
# pattern = re.compile('ab') # it
# print(type(pattern))
# #pattern = 'ab'

matcher = re.finditer('ab','abaabaab')
count = 0
for m in matcher:
    print('pattern found at start:{} end:{} group:{}'.format(m.start(),m.end(),m.group()))
    count = count + 1


print("Total number of coocurance =",count)