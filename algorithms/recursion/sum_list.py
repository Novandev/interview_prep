"""
Sum list

"""

def sum_list(alist, sum=0):

    while len(alist) > 0:
        print(alist[0])
        return sum_list(alist[1:],sum+alist[0])
    print(sum)



if __name__ == "__main__":
    sum_list([1,2,3,4,5])
