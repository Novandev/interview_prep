"""
Factorials are defined as a nuber n in the follwing sequence down to 1

n! = n *(n-1) *(n-2) * (n-3)........ n = 1
"""


def factorial_recursive(val):
    if val < 2:
        return 1
    return(val * factorial_recursive(val -1))



if __name__ == "__main__":
    print(factorial_recursive(5))