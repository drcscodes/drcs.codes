def f():
    global x
    print(x)
    x = 2

def g(x):
    print(x)

if __name__=='__main__':
    x = 1
    f()
    g(x)
