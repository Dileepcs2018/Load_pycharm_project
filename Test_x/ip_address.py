ip_address = "10.001.0040.002"
new_IP = ip_address.split('.')
print(new_IP)
d = 0
l1 = []
for i in new_IP:
    d = int(i)
    # print(d)
    l1.append(d)

#print(l1)
l2 = []
for x in l1:
    l2.append(str(x))

#print("-------",l2)

ip_address = ".".join(l2)
print(ip_address)






