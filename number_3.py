#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.

n = input('Введите число: ')
n_1 = str(n) + str(n)
n_2 = n_1 + str(n)

print (int(n) + int(n_1) + int(n_2))
