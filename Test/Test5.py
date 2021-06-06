import re

s = 'aa HELLO,THere,Hi,How,Are,You....'

#x = re.match("a",s).group()

y = re.findall("[A-Za-z,]{3,}.+",s)
#z = re.search("c.+",s).end()

#print(x)
print("-----------",y)
#print(z)
