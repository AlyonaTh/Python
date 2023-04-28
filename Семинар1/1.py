#Ввести два числа и определить какое число больше

print('Введите первое число: ')
a = int(input())

print('Введите второе число: ')
b = int(input())
if a>b:
    print('a > b')
elif a==b:
    print('a = b')
else:
    print('b > a')
