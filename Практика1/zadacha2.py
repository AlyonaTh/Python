# Найдите сумму цифр трехзначного числа.

a = str(input('Введите трехзначное число: '))
if len(a)!=3:
    print('error')
else:
    sum = 0
    for i in range(3):
        sum += int(a[i])
    print(sum)