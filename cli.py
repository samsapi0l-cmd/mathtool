import argparse

def setup_parse():
    parser = argparse.ArgumentParser(prog="mathtool", description="mathtool позволяет производить математические вычисления.", allow_abbrev=False)
    commands = parser.add_subparsers(dest="command")

    solve = commands.add_parser("solve", help="Решение уравнений по заданным коэффициентам")
    solve.add_argument("-a", type=int, help="коэффициент A: целое число, по модулю не более 10_000")
    solve.add_argument("-b", type=int, help="коэффициент B: целое число, по модулю не более 10_000")
    solve.add_argument("-c", type=int, help="коэффициент C: целое число, по модулю не более 10_000")

    stats = commands.add_parser("stats", help="Показатели числовой последовательности", allow_abbrev=False)
    stats.add_argument("--input", help="Файл, из которого берутся числа (без файла числа берутся со стандартного ввода)")

    integrate = commands.add_parser("integrate",help="Численное интегрирование",allow_abbrev=False)
    integrate.add_argument("--steps", type=int, required=True, help="Число прямоугольников")
    integrate.add_argument("--from", dest="start",type=float, required=True, help="Нижний предел интегрирования")
    integrate.add_argument("--to", type=float, required=True, help="Верхний предел интегрирования")
    integrate.add_argument("--func", choices=["ratio", "root"], type=str, required=True, help="Какую функцию интегрировать")

    series = commands.add_parser("series",help="Сумма числового ряда", allow_abbrev=False)
    series.add_argument("--func", choices=["sqplus", "third"],type=str,help="Какой ряд суммировать",required=True)
    group = series.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="Сколько сложить слагаемых")
    group.add_argument("--eps", type=float, help="Точность остановки")

    return parser