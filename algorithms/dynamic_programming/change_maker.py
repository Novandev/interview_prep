"""
    This problem makes use of the change maker prblem to show off dynamic programming and an example of gready algoriths


    This is where we take the largest choice frist and optimize from there

"""


def change_maker_attempt_1(amount,aList):
    """
    Algorritm
    1. sort the list, and make a dict

    take the largest value and do a modulus. 
    take the value from that ans subtract it from the largest value
    do division to ficure out how many cam come from that
    put that into the dict as the value, and repeat with the num now decreased untill it hits 0
    """
    aList= sorted(aList)[::-1]
    aList_dict = dict()
    for num in aList:
        even_divided = amount - (amount % num)
        print(even_divided)
        aList_dict[num] = even_divided // num
        amount = amount % num
    print(aList_dict)



change_maker_attempt_1(118,[25,10,5,1])
