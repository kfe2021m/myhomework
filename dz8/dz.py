class Time:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def input_time(self):
        self.hours = int(input("Введите часы: "))
        self.minutes = int(input("Введите минуты: "))
        self.seconds = int(input("Введите секунды: "))

    def display_time(self):
        print(f"Время: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

# Пример использования
t = Time()
t.input_time()
t.display_time()