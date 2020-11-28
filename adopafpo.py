a = 0
def lettercheck(x):
    for letterx in str():
        if int(letterx) % 3 != 0:
            return False
    return True


for B in range(100000):
    a = 0
    A = B*B
    if lettercheck(A):
        if lettercheck(B):
            print(B)
            break