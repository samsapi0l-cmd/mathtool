from sys import stdin

def read_numbers(arr):
    nums = []
    for l in arr:
        for x in l.split():
            try: nums.append(float(x))
            except ValueError: raise ValueError(f"{x} не является числом")
    return nums

def stats(args):
    if args.input is None:
        nums = read_numbers(stdin.readlines())
    else:
        nums = read_numbers(open(args.input).readlines())
    print(nums)
        