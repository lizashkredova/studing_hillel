class A(object):
    a = 12
    b = 3
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def mult(cls):
        num = cls.a * cls.b
        return num


# without creating class object
b = A.add(12,12)
print (b)

# with creating class object
# c=A()
# nc=c.add(13,14)
# print(nc)

#classmethod
b=A()
print(b.mult())
