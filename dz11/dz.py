class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        self.h = h
        self.m = m
        self.s = s

    def input_time(self):
        try:
           self.h = int(input("Введите часы: ")) 
           self.m = int(input("Введите минуты: "))
           self.s = int(input("Введите секунды: "))
        except ValueError:
            raise ValueError('Только числа')
        if self.h > 23 or self.m > 59 or self.s > 59 or self.h < 0 or self.m < 0 or self.s < 0:
           raise ValueError('числа вводи')
            
    def __str__(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

# t = Time()
# t.input_time()
# print(t)