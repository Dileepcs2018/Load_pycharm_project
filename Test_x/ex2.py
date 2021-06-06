text = "India is very good country"

new_text = text.split(" ")

output = " "
for word in new_text:
    output = output + word[::-1] + " "


print(output)





