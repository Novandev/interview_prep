#iterative


def sum(n):
    " this will compute the sum of all the numbers leading up to n"
    return (n*(n+1))//2

def sum2(n):
    final_sum =0
    final_sum = [final_sum + x for x in range(n+1)]

    return final_sum




if __name__ == "__main__":
    print(sum(5))
    print(sum2(5))