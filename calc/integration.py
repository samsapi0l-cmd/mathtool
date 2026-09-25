"""Численное интегрирование методом левых прямоугольников."""
import math

MAX_STEPS = 100_000
DIGITS = 4

def F_ratio(x):
    """подынтегральная функция ratio: x / (x + 1)"""
    return x / (x + 1)

def F_root(x):
    """подынтегральная функция root: sqrt(x^2 + 1)"""
    return math.sqrt(x**2 + 1)
#словарик, который содержит функцию ,формулу для пользователя, нижнюю и верхнюю границу и включены ли границы
FUNCTIONS = {
    "ratio": (F_ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root":  (F_root,  "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}

def integral(F, a, b, steps):
    """интеграл функции на [a; b] методом левых прямоугольников"""
    dx = (b - a) / steps
    result = 0
    for i in range(steps):
        x = a + i * dx
        result = result + F(x) * dx
    return result

def integrate(args):
    """обработчик команды integrate"""
    F, formula, low, high, closed = FUNCTIONS[args.func] 
    # проверки различные
    if not math.isfinite(args.start) or not math.isfinite(args.to):
        raise ValueError("Пределы должны быть конечными числами")
    if args.start >= args.to:
        raise ValueError("Начальный предел должен быть меньше конечного")
    if not (1 <= args.steps <= MAX_STEPS):
        raise ValueError(f"Количество шагов вне диапазона от 1 до {MAX_STEPS}")

    if closed: # проверка попадания в промежуток
        if not (low <= args.start <= high) or not (low <= args.to <= high):
            raise ValueError("Предел вне промежутка функции")
    else:
        if not (low < args.start < high) or not (low < args.to < high):
            raise ValueError("Предел вне промежутка функции")

    print(formula)

    result = integral(F, args.start, args.to, args.steps)
    print(f"Значение интеграла: {result:.{DIGITS}f}")
    return 0