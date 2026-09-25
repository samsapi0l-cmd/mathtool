import argparse

def setup_parse():
    parser = argparse.ArgumentParser(prog="mathtool", description="mathtool позволяет производить математические вычисления.", allow_abbrev=False)
    commands = parser.add_subparsers(dest="command")

    solve = commands.add_parser("solve", help="Решение уравнений по заданным коэффициентам")
    solve.add_argument("-a", type=int)
    solve.add_argument("-b", type=int)
    solve.add_argument("-c", type=int)

    stats = commands.add_parser("stats", help="плейсхолдер")
    stats.add_argument("--input", help="плейсхолдер")

    integrate = commands.add_parser("integrate",help="плейсхолдер")
    integrate.add_argument("--steps", type=int, required=True, help="плейсхолдер")
    integrate.add_argument("--from", dest="start",type=float, required=True, help="плейсхолдер")
    integrate.add_argument("--to", type=float, required=True, help="плейсхолдер")
    integrate.add_argument("--func", choices=["ratio", "root"], type=str, required=True)

    series = commands.add_parser("series",help="плейсхолдер", allow_abbrev=False)
    series.add_argument("--func", choices=["sqplus", "third"],type=str, required=True)
    group = series.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="плейсхолдер")
    group.add_argument("--eps", type=float, help="плейсхолдер")

    return parser