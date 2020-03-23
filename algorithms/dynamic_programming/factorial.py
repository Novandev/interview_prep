"""
Factorial in dynamic programming!

"""




def Factorial_dynamic(n):
    memo = [None] * (n+1)
    memo[n-1] = n

    for i in reversed(range(1,n+1)):
        print(i)
        memo[i] = memo[]
Factorial_dynamic(5)