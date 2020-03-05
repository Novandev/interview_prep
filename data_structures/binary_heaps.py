"""
http://ice-web.cc.gatech.edu/ce21/1/static/audio/static/pythonds/Trees/BinaryHeapImplementation.html
The Binary head is a representation of a treestructure as an array 


The binary heap represents a tree as an array.
It keeps it sorted order by use of two functions:

        fixUp:
            From what ever position is added 'i':
                check its parent, and if its less that its parent, swap their positions.
                contine this until youve reached the op of the tree i = 0


        fixDown:
            From the

"""




class BinHeap:
    def __init__(self):
        """
         The heaplist will start off with zero in the first postion to account for the 
         division we wil be doing, since dividing by zero gives an error
        """
        self.heapList = [0]
        self.heapSize = 0 # This will be incremented

    def insert(self,data):
        """
        
        """
        self.heapList.append(data)
        self.heapSize = self.heapSize + 1
        self.fixUp(self.heapSize)


    def fixUp(self,i):
        """
            The fix up takes the last element in the array and checks its parents 
            value. if the parent value is more than the 

        """
        while i // 2 > 0: # Makes the counter stop at self.heapList[0] as to not run over
            if self.heapList[i] < self.heapList[i // 2]: # If the node were currently at is less than the parent
                tmp = self.heapList[i // 2] # Make a temorary variable holding the contents of the parent
                self.heapList[i // 2] = self.heapList[i] # Overwrite the contents of the variable we're curently at with the contents of parent
                self.heapList[i] = tmp # Drop the contents of temporary vairable (originally the parents of the content were currently at, but used to be at)
                # to the actual position of the content we used to be at
            i = i // 2
    