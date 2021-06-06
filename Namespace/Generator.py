def genarator():
    print("before execution")
    for i in range(10):
        yield i
        print("wow",i)
    print("After resuming next execution")

#this dileep to push into git hub
it = genarator()
print(it.__next__())
print(it.__next__())
print(it.__next__())