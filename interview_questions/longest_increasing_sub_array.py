"""
The longest increasing sub array

Given an array get the longest increasig sub array

ex

[-1,2,4,5,2,2,2,2,2]

the longest increasing sub array would be [2,2,2,2,2]

Algorithm(naive, my own)

This is an example of a good dynamic programming 
Solution 1
start with an array the same size as the original size but fill it with ones


"""


def longest_increasing_sub_array(aList):

    counter = len(aList) * [1]
    i,j = 0,1





longest_increasing_sub_array([-1,2,4,5,2,2,2,2,2])