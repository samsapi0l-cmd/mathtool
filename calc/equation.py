from math import sqrt

def solve(a,b,c): #здесь мы решаем уравнение
    x1 = x2 = None #проинициализируем корни, но без значения

    #equation = f"{f"{a}x^2" if a != 0 else ""}{f"{"" if a == 0 else ("" if b < 0 else ("+" if a != 0 else ""))}{b}x" if b != 0 else ""}{f"{"+" if c > 0 else ""}{c}" if c != 0 else ""}=0" # составление уравнения зная коэффициенты, просто много форматирования с условиями
    #print(f"Работа с {"линейным" if a == 0 else "квадратным"} уравнением: {equation}")
    #решил убрать пока что вывод уравнения, поскольку не знаю куда его пристроить по тз
    # решаем уравнения
    if a == 0: # линейное уравнение, решаем обычным уединением радикала
        x1 = -c/b

        return ["линейное", "отсутствует",[x1]]
    else: # квадратное уравнение, вычисляем дискриминант и действуем взависимости от его знака
        d = b*b - 4*a*c
        if d > 0:# находим оба корня т.к. дискриминант положительный
            x1 = (-b + sqrt(d)) / (2*a)
            x2 = (-b - sqrt(d)) / (2*a)
            return ["квадратное", d,[x1,x2]]
        elif d == 0: # находим один корень, т.к. дискриминант равным нулю
            x1 = -b / (2*a)
            return ["квадратное", d,[x1]]
        else: return ["квадратное", d, []] # нет корней поскольку дискриминант отрицательный

def checkAndTransform(a): # проверяет является ли содержимое строки целым числом, если нет то возвращает "error", если да то возвращает само число
    if "." in a or "," in a: return "error"
    else: 
        try: return int(a); # try/except на случай если пользователь отправит abc вместо числа
        except ValueError: raise ValueError("Коэффициент не является целым числом!")

def prepareAndSolve(args): # здесь мы проверяем и обрабатываем все данные и далее отправляем на решение в функцию solve
    MAX_VALUE = 10000 # диапазон, который могут принимать коэффициенты
    if args.a is None and args.b is None and args.c is None:
        A,B,C = checkAndTransform(input("Введите A: ")),checkAndTransform(input("Введите B: ")),checkAndTransform(input("Введите C: ")) # принимаем ввод от пользователя
    elif args.a is not None and args.b is not None and args.c is not None:
        A,B,C = args.a,args.b,args.c # присваиваем переменным значения параметров
    else: raise ValueError("Не хватает одного из коэффициентов!")
    if A != "error" and B != "error" and C != "error": # проверяем, являются ли полученные данные целыми числами
        if abs(A) <= MAX_VALUE and abs(B) <= MAX_VALUE and abs(C) <= MAX_VALUE: #проверяем, входят ли все коэффициенты в допустимый диапазон
            if A == 0 and B == 0:
                raise ValueError("Коэффициенты A и B вместе не могут быть равны нулю!")
            else: 
                results = solve(A,B,C) #отправляем коэффициенты в функцию solve, где будет решаться составленное на их основе уравнение
                radicals = results[2] # получаем список корней из solve
                print(f"Вид уравнения: {results[0]}\nДискриминант: {results[1]}")
                if len(radicals) == 0: print("Нет действительных корней")
                elif len(radicals) == 1: print(f"X = {radicals[0]}")
                else:
                    for i in range(2):
                        print(f"X{i+1} = {radicals[i]}") # выводим все корни по порядочку
                return 0
        else: raise ValueError(f"Коэффициенты должны быть по модулю не более {MAX_VALUE}!")
    else:  raise ValueError("Неверно введены коэффициенты!")
