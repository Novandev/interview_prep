"""
Given two sorted lists

The first in descending and the second in ascending
example [100,80,50] and [40, 60, 110]

find positions of all elements, returned as a list


"""
def recBinarySearch( target, theSeq, first, last ):
# If the sequence cannot be subdivided further, we are done.
    if len(theSeq[first:last])<3:
        print(theSeq[first:last])
    else :
        # Find the midpoint of the sequence.
        mid = (last + first) // 2
        # Does the element at the midpoint contain the target?
        if theSeq[mid] == target :
            return mid
            # base case #2
        # or does the target precede the element at the midpoint?
        elif target > theSeq[mid] :
            return recBinarySearch( target, theSeq, first, mid - 1 )
        # or does it follow the element at the midpoint?
        else :
            return recBinarySearch( target, theSeq, mid + 1, last )





def find_position_of_elements(list_1,list_2):
    position_list =list()
    stop = False

    first_item = list_2[0]
    if first_item > list_1[0]:
        return [2,1,0]
    if first_item < list_1[len(list_1) - 1]:
        return[len(list_1)-1,len(list_1)-2,len(list_1)-3]
    starting_postion = recBinarySearch(list_2[0],list_1,0,len(list_1)-1)

    print(starting_postion)




find_position_of_elements([100,90,80,74,50,30,20],[40, 60, 110])


