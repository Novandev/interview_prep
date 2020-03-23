"""


"""


def fibonacciVal(n):
    memo = [0] * (n+1)
    memo[0], memo[1] = 0, 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    # print(memo[n])
    return memo[n]


print(fibonacciVal(5))