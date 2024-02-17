class Time:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def input_time(self):
        while True:
            self.hours = int(input("Введите часы: "))
            self.minutes = int(input("Введите минуты: "))
            self.seconds = int(input("Введите секунды: "))
            if self.hours > 23 or self.minutes > 59 or self.seconds > 59:
                print('no')
            else:
                break
            

    def __str__(self):
        return f"Время: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


t = Time()
t.input_time()
print(t)