import math

def square(side):
    return math.ceil(side*side)

side = float(input("Введите размер стороны: "))
print(f'Округленная в большую сторону сумма - {square(side)}')


