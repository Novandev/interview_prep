"""
Print vall shwoing off recursion

"""

def print_val_before(val):

    if val > 0:
        print(val)
        return print_val_before(val-1)

def print_val_after(val):

    if val > 0:
        return print_val_after(val-1)
        print(val)

if __name__ == "__main__":
    print_val_after(4)

    # print_val_before(4)