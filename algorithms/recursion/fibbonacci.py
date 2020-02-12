"""
Fibbonacci Sequence
this will compute the nth fibbonacci number
"""


def fibbonacci(val):
    # print(/val)
    if val <= 2:
        return 1
    else:
        return fibbonacci(val-1) + fibbonacci(val-2)
if __name__ == "__main__":

    print(fibbonacci(20))