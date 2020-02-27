"""


    

"""



def permutation_maker(a, n, k, depth, used, current_permutation = [], permutations = []):
  '''
  Implement permutation of k items out  of n items

  a: the list we will make permutations out of
  n: the length of the list as a sentonel value
  k: The sentinel value that tracks how deep the recursion should go
  depth: start from 0, and represent the depth of the search
  used: track what items are  in the partial solution from the set of n
  current_permutation: the current partial solution
  permutations: collect all the valide solutions
  

  Algorithm:
    1. check the base case of k, if k ( the number of times we want the permutation to run) is equal to the depth
    if it does appendthe list that we will make below to the permutations array, with a deep copy and return
    2. for each element in the array
        if in the used array, the position hasnt been processed:
            append the current variable to the current permutation
            set the position of this in the used array to True to signalits been processed
            recurse the function, but increse the depth

  '''
  if depth == k: #if the "depth" is equal to the lenth of the list
    permutations.append(current_permutation[::]) # use deepcopy because current_permutation is tracking all partial solution, it eventually become []
    return
  
  for i in range(n):
    print(i)
    print(used)
    if not used[i]:
      # generate the next solution from curr
      current_permutation.append(a[i])
      used[i] = True
      print(current_permutation)
      # move to the next solution
      permutation_maker(a, n, k, depth+1, used, current_permutation, permutations)
      
      #backtrack to previous partial state
      current_permutation.pop()
      print('backtrack: ', current_permutation)
      used[i] = False
  return

a = [1, 2, 3,4]
n = len(a)
k = len(a)
# Used is a list that will track wether or not
used = [False] * len(a)
ans = []
permutation_maker(a, n, k, 0, used, [], ans)
print(ans)