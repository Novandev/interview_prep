"""
Fibbonacci Sequence
this will compute the nth fibbonacci number
"""


def fibbonacci(val):
    if val <= 1:
        return 1
    else:
        return fibbonacci(val-1) + fibbonacci(val-2)
if __name__ == "__main__":
    for i in range(7-1):
        print(fibbonacci(i))