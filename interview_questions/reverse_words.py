"""
Reverse Words.
take a string of words such as
" string of words"
 and return
 "words of string"

 make sure to trim any white spaces
Algorithm:
1. make a sentinel string  that will track a current "word" out of a string
a "word" is defined as a set of characters withour a space, so if spaces are skipped
we can keep track of the word

2. Well need something to store all the values form the interation of a word this will be an array called words

3. after a word has been added, set the sentinel back to an empty string

4. if theres still a word left over add it to the array

5 reverse this array

6 join the array by a space and return it



"""

def reverse_words(string:str):
    current_word = ""
    word_array = list()

    for char in string:
        if char !=" ":
            current_word += char
        else:
            word_array.append(current_word)
            current_word = ""
    if current_word:
        word_array.append(current_word)


    word_array.reverse()
    print(" ".join(word_array))

reverse_words(" string of words")

