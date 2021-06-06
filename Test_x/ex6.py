for line in open("python_text"):
    li = line.strip()
    if not li.startswith("#"):
        print(li)
