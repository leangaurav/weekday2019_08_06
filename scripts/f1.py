x = 100

def my_abs(x):
    if x < 0:
        x = -x
    return x

if __name__ == '__main__': # 'f1'
    print(x)

    print(my_abs(10))
    print(my_abs(-10))
    print(__name__)
    print(abs.__name__)