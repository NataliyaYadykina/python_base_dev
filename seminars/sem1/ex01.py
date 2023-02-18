# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

day_distance = int(input('За день машина проезжает дней: '))
total_distance = int(input('Длина всего маршрута: '))

days = int((total_distance + day_distance - 1) / day_distance)

print(f'Расстояние {total_distance} машина проедет за {days} дней.')
