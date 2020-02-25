"""


    

"""



def permutation_maker(a, n, k, depth, used, current_permutation = [], permutations = []):
  '''
  Implement permutation of k items out  of n items
  depth: start from 0, and represent the depth of the search
  used: track what items are  in the partial solution from the set of n
  curr: the current partial solution
  ans: collect all the valide solutions
  '''
  if depth == k: #end condition
    permutations.append(current_permutation[::]) # use deepcopy because current_permutation is tracking all partial solution, it eventually become []
    return
  
  for i in range(n):
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
  return permutations

a = [1, 2, 3]
n = len(a)
# ans = [[None]]
# Used is a list that will track wether or not
used = [False] * len(a)
ans = []
permutation_maker(a, n, n, 0, used, [], ans)
print(ans)