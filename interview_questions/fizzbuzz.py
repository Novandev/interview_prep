"""
Fizzbuzz question
Take all numbers from 1-n
If a number is amultple of 3 return fizz, if it is a multiple of 5 return buzz else fizzbuzz

Algorithm:
 1. if a numer is divisible by 3 and not 5: print fizz
 2. If a number is divisible by 5 and not 3: print buzz
 3. if a number is divisible by both: print fizzbuzz

"""



def fizz_buzz(n:int):
    for i in range(1,n+1):
        if i % 3 ==0 and i % 5 !=0:
            print("Fizz")
        if i % 5 == 0 and i % 3 !=0:
            print("Buzz")
        if i % 5 == 0 and i % 3 == 0:
            print("fizzbuzz")

fizz_buzz(15)