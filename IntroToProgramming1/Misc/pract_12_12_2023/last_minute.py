class A:
    def __init_(self):
        self.a = 1
        self.__b = 1
    def __str__(self):
        return str(self.a) + "" + str(self.__b)

a = A()
print(a)
print(a.a)
print(a.A.__b)