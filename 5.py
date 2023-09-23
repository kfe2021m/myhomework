x = int(input())
y = int(input())
if x == 0:
    print('точка лежит на оси x')
elif y == 0:
    print('точка лежит на оси y')
elif x > 0 and y > 0:
    print('первая четверть')
elif x < 0 and y > 0:
    print('вторая четверть')
elif x < 0 and y < 0:
    print('третья четверть')
elif x > 0 and y < 0:
    print('четвертая четверть')  
