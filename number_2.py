#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_second = int (input('Введите время в секундах: '))
hour = time_second // 3600
minute = (time_second // 60) % 60
second = time_second % 60

if hour < 10:
    h = ('0' + str(hour))
else: h = str(hour)

if minute < 10:
    m = ('0' + str(minute))
else: m = str(minute)

if second < 10:
    s = ('0' + str(second))
else: s = str(second)

print(f'{h}:{m}:{s}')

