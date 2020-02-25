"""
1.Give a number n that represents the length a substring can be, fine the repeats

2.start out with two sets one for things that have been seen and one for things that have been repeated

3. Start and interation , stopping at the length of the string minus n, this is to stop the array from
running over

4. check if all of the characters from the current position to n from that position are in seen,
    if they are :
        add them to repeat
    if not:
        add them to seen

5 return the repeat array

"""




def repeated_substring(string:str, n:int):

    seen1 = set()
    seen2 = set()
    for i in range(len(string)-n+1):
        print(string[i:i+n])
        if string[i:i+n] in seen1:
            seen2.add(string[i:i+n])
        else:
            seen1.add(string[i:i+n])
    print(seen2)

repeated_substring("aaaaaccc",2)