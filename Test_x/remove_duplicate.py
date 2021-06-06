intput1 = "ABC"
input2  = "BANGALORE"

output1 = " "
output2 = " "
for i in intput1:
    if i not in input2:
        output1 = output1 + i

for j in input2:
    if j not in intput1:
        output2 = output2 + j

print(output1)
print(output2)


final = output1 + output2

print(final)

