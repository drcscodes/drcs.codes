import sys

def fahrenheit2celsius(f: int) -> float:
    return 5 * (f - 32) / 9

def main(args: list[str]) -> None:
    if len(args) > 1:
        lower = int(args[1])
    else:
        lower = 0
    upper = int(args[2]) if len(args) > 2 else 300
    step = int(args[3]) if len(args) > 3 else 20

    print(f"Fahrenheit Celsius")
    print(f"---------- -------")
    for f in range(lower, upper, step):
        c = fahrenheit2celsius(f)
        print(f"{f:<10} {c:>7.1f}")

if __name__=='__main__':
    print(sys.argv)
    main(sys.argv)
