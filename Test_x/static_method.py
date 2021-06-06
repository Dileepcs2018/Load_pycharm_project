class A:
    num =10
    @classmethod
    def show(cls):
        cls.num =100
        print(cls.num)

    def b(self):
        self.d = 'a'
        print(self.d)



# a  = A()
# a.show()
#A.num
# print(a.num)
A.show()
print(A.num)
print(A.b())
