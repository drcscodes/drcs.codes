import sys

def add(x: int, y: int) -> int:
    return x + y

def sub(x: int, y: int) -> int:
    return x - y

if __name__=="__main__":
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[2])
    ops = {"+": add, "-": sub}
    result = ops[op](a, b)
    print(result)
