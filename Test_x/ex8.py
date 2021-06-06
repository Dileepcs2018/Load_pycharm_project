s = "this is permanant number"
d = {}
sub = "this"
if sub in s:
    print("present")

else:
    print("Not present")
count = 0
for i in s:
    if i in ['a','e','i','o','u']:
        count = count + 1

print(count)


