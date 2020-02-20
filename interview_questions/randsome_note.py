from collections import Counter
"""
    A randsome note can be made by a bag of string charaters
    find if a second bag of strigs can be used to make the same radsome note

    solution:
    turn both into a hastable and check if thay are 
    lets use thecounter class from collections

"""



def _check_randsome_note(str_1,str_2):
    str_1 = str_1.replace(" ","").lower()
    str_2 = str_2.replace(" ","").lower()
    counter_1 = Counter()
    counter_2 = Counter()
    for item in str_1:
        counter_1[item] +=1
    for item in str_2:
        counter_2[item] +=1
    print(counter_2)
    print(counter_1)
    return counter_1 == counter_2


print(_check_randsome_note('You and I','ouY dan I'))