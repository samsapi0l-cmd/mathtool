from sys import argv
from sys import exit
def help(): # функция выводящая справку и завершающая программу
    print("Mathtool позволяет решать алгебраические уравнения вида  A·x² + B·x + C = 0, \n" \
    "Использование: \n " \
    "python mathtool.py ИЛИ python mathtool.py --help    вывод справки\n " \
    "python mathtool.py solve    ввод коэффициентов с клавиатуры\n " \
    "python mathtool.py solve -a <a> -b <b -c <c>    решение с заданными коэффициентами")
    exit(0)

def solve(a,b,c): #функция решающая уравнение по коэффициентам
    print("solve placeholder") #плейсхолдер чтобы не ругалось
def checkAndTransform(a): # проверяет является ли содержимое строки целым числом, если нет то возвращает "error", если да то возвращает само число
    if "." in a or "," in a: return "error"
    else: return int(a)
def main():
    match(len(argv)): # смотрим аргументы по их количеству
        case 1:
            help()
        case 2:
            if argv[1] == "--help":
                help()
            elif argv[1] == "solve":
                try: 
                    A = checkAndTransform(input("Введите число A:"))
                    B = checkAndTransform(input("Введите число B:"))
                    C = checkAndTransform(input("Введите число C:"))
                    if A != "error" and B != "error" and C != "error":
                        if A in range(-10000,10001) and B in range(-10000,10001) and C in range(-10000,10001):
                            if A == 0 and B == 0:
                                exit("ОШИБКА! Коэффициенты A и B вместе не могут быть равны нулю!")
                            else: 
                                pass # сюда функцию solve потом
                        else: exit("ОШИБКА! Коэффициенты должны быть по модулю не более 10_000!")
                    else: exit("ОШИБКА! Неверно введены коэффициенты!")
                except Exception: exit("ОШИБКА! Коэффициент не является целым числом")
            else:
                exit("ОШИБКА! Неверный аргумент")
        case 8:
            pass # воткнуть solve пропарсив аргументы
        case _:
            exit("ОШИБКА! Неверное количество аргументов")
    exit(0)
if __name__ == "__main__":
    main()