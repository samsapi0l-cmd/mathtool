import sys
from calc.equation import prepareAndSolve
from calc.stats import stats
from calc.series import series
from calc.integration import integrate
import cli

def main(argv):
    parser = cli.setup_parse() # настраиваем парсер
    args = parser.parse_args(argv) # скармливаем ему аргументы

    if args.command is None: 
        parser.print_help() # если нет никаких аргументов, выводим справку
        return 0

    handlers = { # словарь с названиями команд и соответствующими функциями
        "solve" : prepareAndSolve,
        "stats" : stats,
        "series" : series,
        "integrate" : integrate
    }
    try:
        return handlers[args.command](args) #вызывает нужную команду, передавая аргументы, чтобы они могли посмотреть нужные параметры
    except (ValueError, OSError) as error:
        print(f"ОШИБКА! {error}", file=sys.stderr) #если что-то выдало ошибку, оно её получит и напечатает
        return 1
    
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) # вызываем main, помещая туда аргументы исключая название файла, и завершает программу с кодом, который вернул main