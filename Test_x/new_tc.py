
# initializing string
test_string = "There are 2 apples for 4 persons"

new_str = test_string.split()
output = " "
output1 = " "
for i in new_str:
    if i.isdigit():
        output = "" + output + i + " "

    else:
        output1 = output1 + i


print(output)




