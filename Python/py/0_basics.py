"""
0_basics.py

"""
def hw_1():
    for i in range(2, 10):
        for j in range(1, 10):
            print(f"{i:2d} x {j:2d} = {i*j:2d}", end='  ')
        print()


# hw_1()

def hw_2():
    for i in range(10):
        for j in range(i, 10):
            print("*", end='')
        print()
# hw_2()


# when h = 3
#
# 0 *******
# 1 *** ***
# 2 **   **
# 3 *     *
# 4 **   **
# 5 *** ***
# 6 *******
#
def hw_3():
    H = 5

    print("*" * (H*2 + 1))

    for i in range(H):
        print(
            "*" * (H-i) +
            " " * (i*2+1) +
            "*" * (H-i))

    for i in range(2, H+1):
        print(
            "*" * (i) +
            " " * ((H-i)*2+1) +
            "*" * (i))

    print("*" * (H*2 + 1))

hw_3()
