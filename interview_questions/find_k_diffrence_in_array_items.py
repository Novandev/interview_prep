"""
This algorithm takes an unsorted array arr and a value k and finds the item pairs in tha array that if subtracted,
 match k this is then added to the array as both the element and the element minues the subtracted value

"""



def _find_same_difference(arr,k):
    arr_dict = dict.fromkeys(arr)
    for element in arr:
        if element - k in arr_dict:
            print(element,element-k)



_find_same_difference([1,7,5,9,2,12,3],2)