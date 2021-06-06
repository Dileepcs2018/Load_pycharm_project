import json

f = open("x.txt","w")
data = {'dileep':5000,'ravi':8000}

json.dump(data,f)