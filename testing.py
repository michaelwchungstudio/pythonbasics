class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        if self.num <= 20:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration

numbers = MyNumbers()
numiter = iter(numbers)

for x in numiter:
    print(x)