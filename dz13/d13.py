class Time:
    def init(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def input_time(self):
        try:
            self.h = int(input("Введите часы: "))
            self.m = int(input("Введите минуты: "))
            self.s = int(input("Введите секунды: "))
        except ValueError:
            raise ValueError("Вводите нормальные значения!!!!!") 

        if self.h > 23 or self.m > 59 or self.s > 59 or self.h < 0 or self.m < 0 or self.s < 0:
            raise ValueError("Что-то не правильно")   

    def add(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        
        if total_seconds >= 24 * 3600:
            total_seconds -= 24 * 3600
        
        return self.from_seconds(total_seconds)
  
    def sub(self, other):
        total_seconds = self.to_seconds() - other.to_seconds()

        if total_seconds < 0:
            total_seconds += 24 * 3600
        

        return self.from_seconds(total_seconds)

    def to_seconds(self):
        return self.h * 3600 + self.m * 60 + self.s
    
    def from_seconds(self, seconds):
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds = seconds % 60

        return Time(hours, minutes, seconds)
    
    def eq(self, other):
        return self.h == other.h and self.m == other.m and self.s == other.s

    def ne(self, other):
        return not self == other

    def str(self):
       return f"Время: {self.h:02d}:{self.m:02d}:{self.s:02d}" 

t1 = Time()
t2 = Time()


# t1.input_time()
# t2.input_time()


result_sum = t1 + t2
print("Сумма времен:", result_sum)

result_diff = t1 - t2
print("Разница времен:", result_diff)