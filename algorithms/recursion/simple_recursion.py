"""
This shows off a few examples of simple recursion

"""
branches = ["Branch 1", "Branch 2", "Branch 3", "Branch 4"]



def print_branches_recursively(branches):
    """
    Each call of this function is on a diffrent "branch"
    """
    #represents the base case for recursion and there for prints
    # print(branches[0])
    if len(branches) == 1:
        branch = branches[0]
        # print(branch)

    else:
        mid_point = len(branches) // 2
        first_half = branches[:mid_point]
        second_half = branches[mid_point:]

        print(first_half)
        print(second_half)


        print_branches_recursively(first_half)
        print_branches_recursively(second_half)

if __name__ == "__main__":
    print_branches_recursively(branches)


