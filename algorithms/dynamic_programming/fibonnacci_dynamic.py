"""
Dynamic programming and Memoization

"""


def fibonacci_dynamic(n):
    '''
    This function displayes the proper use of memoization 
    
    '''
    pass


def fibonacci_recursion(n):
    '''
        SO recursion is usually a place to start  with this kinda stuff
        The problem is that it builds a tree so larger values end up being intractable

        fib(7) ={
            6{
                5:{
                    4
                    3"
                }
                4:{
                    2
                    3
                }
            }
            5:{

            }
        }

        This means that it tends to repeat steps, so we'll need to cut down on that
    
    This is 2^n

    so fibonacci_recursion(50) == 2^50 YIKES
    '''
    print(n-1, n-2)
    # Base case
    if n <= 2:
        return 1
    
    return fibonacci_recursion( n - 1) + fibonacci_recursion( n- 2)


if __name__ == "__main__":

    print(fibonacci_recursion(7))