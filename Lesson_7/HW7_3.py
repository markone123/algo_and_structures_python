"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
from random import random
m = int(input("Введите m: "))
N = 2*m+1
arr = []
for i in range(N):
        arr.append(int(random() * 50))
print(arr)

#Вариант 1
import statistics
print(statistics.median(arr))

#Вариант 2
def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0
print(median(arr))

#Вариант 3
def partition(a, i, j):
    v = a[(i + j)//2]       
    while i <= j:
        while a[i] < v:
            i += 1
        while a[j] > v:
            j -= 1
        if i <= j:
            a[i],a[j] = a[j],a[i]
            i += 1
            j -= 1
    return j
 
def mediana(a):
    k, left, right = len(a)//2, 0, len(a)-1
    while(True):
        mid = partition(a, left, right)
 
        if mid == k:
            return a[mid]
 
        if k < mid:
            right = mid
        else:
            left = mid + 1
print(mediana(arr))
            
