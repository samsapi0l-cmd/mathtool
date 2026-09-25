import math

MAX_TERMS = 10_000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100_000
DIGITS = math.ceil(-math.log10(MAX_EPS))

def sign(n):
    """Возвращает +1 для нечётных чисел и -1 для чётных"""
    if n % 2 == 1:
        return 1
    else: return -1

def term_sqplus(n):
    """n слагаемое ряда для sqplus: sign(n) / (n*n + 1)"""
    return sign(n) / (n * n + 1)

def term_third(n):
    """n слагаемое ряда для third: sign(n) / (3 * n)"""
    return sign(n) / (3 * n)

FORMULAS = { #словарик, который содержит функцию для слагаемого и формулу для пользователя
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third":   (term_third,  "S = 1/3 - 1/6 + 1/9 - 1/12 + ..."),
}

def sum_by_terms(term, count):
    """Сумма первых столько-то(count) слагаемых. term - функция для слагаемого"""
    total = 0
    for n in range(1, count + 1):
        total = total + term(n)
    return total

def sum_by_eps(term, eps):
    """Сумма до достижения точности(eps). Возвращает сумму и кол-во слагаемых."""
    total = 0
    for n in range(1, MAX_ITERATIONS + 1): # чтобы не зациклилось если что, если не понравится то выплюнет ошибку
        value = term(n)
        total = total + value
        if abs(value) < eps: # если слагаемое слишком маленькое
            return total, n
    raise ValueError("точность не достигнута")

def series(args):
    """Считает сумму выбранного ряда и выводит формулу, кол-во слагаемых и сумму"""
    term, formula = FORMULAS[args.func]

    if args.terms is not None:
        if not (1 <= args.terms <= MAX_TERMS):
            raise ValueError(f"Количество слагаемых вне диапазона от 1 до {MAX_TERMS}")
    else:
        if not math.isfinite(args.eps) or not (0 < args.eps <= MAX_EPS):
            raise ValueError(f"Точность вне диапазона от 0 до {MAX_EPS}")

    print(formula)
    if args.terms is not None:
        summ = sum_by_terms(term, args.terms)
        count = args.terms
    else:
        summ, count = sum_by_eps(term, args.eps)

    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {summ:.{DIGITS}f}")
    return 0