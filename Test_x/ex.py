
import re

text = "this is my first job"

x = re.search("^this.*job$",text)

if x:
    print("found")