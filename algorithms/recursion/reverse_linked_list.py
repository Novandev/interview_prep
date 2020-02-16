"""
Recursive soution for reversing a linked list this shows how the call stack works

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


LLnode1 = Node(data =1)
LLnode2 = Node(data =2)
LLnode3 = Node(data =3)
LLnode4 = Node(data =4)
LLnode5 = Node(data =5)
LLnode1.next = LLnode2
LLnode2.next = LLnode3
LLnode3.next = LLnode4
LLnode4.next = LLnode5
LLnode5.next = None

def print_ll_reverse(node):

    if node.next is not None:
        print_ll_reverse(node.next)
        print(node.data)


if __name__ == "__main__":
    print_ll_reverse(LLnode1)