"""
Recursive solution to doing exponents
"""


def exp(val,exponent):
    """
    Since doing large exponents results in a forloop and alot of processing
    """
    if exponent == 0:
        return 1
    result = exp(val *val, exponent // 2)

    if result % 2 == 0:
        return result
    else:
        return result * val


if __name__ == "__main__":
    print(exp(8,2))