"""
Given an array of numbers and a value, return all of the combibation of
numerbs that add up the the given value


Algorithm:
    Make a array to store the values

1. make a dictionary/hashtable out of the array O(N) time and space
2. interatre over the array
    for each value in the array O(N)
        if the element minus k is a value on the dictionary O(1)
        add the element and the element - the value to a tuple and\
        append this to the array of stored values

3. return the array of store values

"""



def _find_same_difference(arr,k):
    arr_dict = dict.fromkeys(arr)
    for element in arr:
        if element - k in arr_dict:
            print(element,element-k)



_find_same_difference([1,7,5,9,2,12,3],2)