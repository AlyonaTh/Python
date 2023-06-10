# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
list = [0, -1, 5, 2, 3, 8, 5, 7]
count = 0
for i in range(1, len(list)):
    if list[i-1] < list[i]:
        count += 1
print(count)