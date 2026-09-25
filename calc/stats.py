from sys import stdin
from sys import argv
from math import isfinite
from math import sqrt
def read_numbers(arr):
    # 12 13 14 \n
    MAX_VALUE = 10_000
    nums = [] # инициализируем список
    for l in arr: # для каждой строки
        for x in l.split(): # для каждого элемента в строке
            print(x)
            try: nums.append(float(x.replace(',','.'))) # тз того не требует конечно, но позволяет обработать числа вида 1,2 а не только 1.2
            except ValueError: raise ValueError(f"{x} не является числом")
    if len(nums) == 0: raise ValueError("Полученный список пуст")
    if len(nums) > 20: raise ValueError("Количество элементов в списке больше 20")
    if any(not isfinite(x) for x in nums): raise ValueError("Числа должны быть конечными(не принимаются inf, nan, -inf)")
    if any(abs(x) > MAX_VALUE for x in nums): raise ValueError(f"Числа должны быть по модулю не более {MAX_VALUE}!")
    return nums
# различные функции
def avrg(nums): # среднее арифметическое
    return sum(nums)/len(nums)

def positive_count(nums): # кол-во положительных чисел
    return len([x for x in nums if x > 0])

def negative_count(nums): # кол-во отрицательных чисел
    return len([x for x in nums if x < 0])

def squared_devia_sum(nums): # сумма квадратов отклонений чисел от их среднего арифметического
    average = avrg(nums)
    return sum([(x - average)**2 for x in nums])

def variance(nums): # дисперсия
    return squared_devia_sum(nums)/len(nums)

def standard_devia(nums): # стандартное отклонение
    if len(nums) < 2: return None
    return sqrt(squared_devia_sum(nums)/(len(nums)-1))

def sqr_sum(nums): # сумма квадратов чисел
    return sum([x**2 for x in nums])

def root_mean_sqr(nums): # среднее квадратическое
    return sqrt(sqr_sum(nums)/len(nums))

def std_dev(nums): #ско (среднеквадратическое отклонение)
    return sqrt(variance(nums))

def stats(args):
    
    if args.input is None: # если нет параметра --input, то читает ввод пользователя
        #nums = read_numbers(stdin)
        array = []
        while True:
            s = input()
            if s == "" and len(array) != 0: nums = read_numbers(array); break
            elif s == "" and len(array) != 0: raise ValueError("ошибка")
            array.append(s)
    else: 
        with open(args.input, encoding="utf-8") as f: #читает файлик
            nums = read_numbers(f)
    params_table = [ # таблица характеристик
        ("Количество", len, "d"),
        ("Сумма", sum, ".3f"),
        ("Ср. арифм.", avrg, ".3f"),
        ("Сумма кв.", sqr_sum, ".3f"),
        ("Ср. кв.", root_mean_sqr,".3f"),
        ("Дисперсия", variance,".3f"),
        ("СКО", std_dev,".3f"),
        ("Станд. откл.",standard_devia,".3f"),
        ("Наименьшее", min, ".3f"),
        ("Наибольшее", max, ".3f"),
        ("Положительных",positive_count, "d"),
        ("Отрицательных", negative_count, "d")
    ]
    for label, function, form in params_table: # распаковка и принт
        value = function(nums)
        if value is None: print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else: print(f"{label}: {value:{form}}")


if __name__ == "__main__":
    stats(None)