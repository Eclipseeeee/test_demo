class A:
    def __init__(self):
        self.aaa = 1

    def func_a(self, x):
        return x + self.aaa

isinstance_a = A()
print(isinstance_a.func_a(2))