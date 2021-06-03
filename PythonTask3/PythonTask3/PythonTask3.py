import math
import numpy
import random
import statistics as stat
print(help(math))
print(dir(math))

list = [13,23,38,44,155,68,72,81,90,100]
print(list)
print("Сумма цифр: ", math.fsum(list))
print("Среднее: ", statistics.mean(list))
print("Медиана: ", statistics.median(list))
print("Стандартное отклонение: ", statistics.stdev(list))



#print("Random integer between 1 and 100: ", ran.randint(1,100))