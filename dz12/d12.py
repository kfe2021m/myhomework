class Time:

    def init(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def validate(self):
        self.hours = int(input("Введите часы: "))
        self.minutes = int(input("Введите минуты: "))
        self.seconds = int(input("Введите секунды: "))
        if 0 <= self.hours < 24 and 0 <= self.minutes < 60 and 0 <= self.seconds < 60:
            return True
        else:
            return False
        
    def str(self):
       return f"время: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}" 

# Создание объекта и проверка валидности
t = Time()
if t.validate():
    print("Время введено корректно: ", t)
else:
    print("Время введено некорректно.")