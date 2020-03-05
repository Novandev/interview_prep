
def all_possible_permutation_array(a, n, depth, used, current_permutation = [], permutations = []):
  '''
  Implement permutation of k items out  of n items

  a: the list we will make permutations out of
  n: the length of the list as a sentonel value
  depth: start from 0, and represent the depth of the search
  used: track what items are  in the partial solution from the set of n
  current_permutation: the current partial solution
  permutations: collect all the valide solutions
  

  Algorithm:
    1.  append to the result of the current purmeutation to the deep copied current permutation array,
     becuase there is no stopping point, it will get all posible combinations
    2. for each element in the array
        if in the used array, the position hasnt been processed:
            append the current variable to the current permutation
            set the position of this in the used array to True to signalits been processed
            recurse the function, but increse the depth

  '''
  permutations.append(current_permutation[::]) # use deepcopy because current_permutation is tracking all partial solution, it eventually becomes []
  
  for i in range(n): # go over every variable in ever recursive call
    print(i)
    print(used)
    if not used[i]: # If the used array that tracks whats been used in the recursive call for this iteration of n hasent been done
      current_permutation.append(a[i]) # To the current permutation array, append the data at the current postision to the array we're in
      used[i] = True # For this current iteration 
      print(current_permutation)
      # move to the next solution
      permutation_maker(a, n, depth+1, used, current_permutation, permutations)
      
      # When the recursion has finished
      current_permutation.pop()
      print('backtrack: ', current_permutation)
      used[i] = False
  return




def all_possible_permutation_string(a, n, depth, used, current_permutation = '', permutations = ''):
  '''
  Implement permutation of k items out  of n items

  a: the list we will make permutations out of
  n: the length of the list as a sentonel value
  depth: start from 0, and represent the depth of the search
  used: track what items are  in the partial solution from the set of n
  current_permutation: the current partial solution
  permutations: collect all the valide solutions
  

  Algorithm:
    1.  append to the result of the current purmeutation to the deep copied current permutation array,
     becuase there is no stopping point, it will get all posible combinations
    2. for each element in the array
        if in the used array, the position hasnt been processed:
            append the current variable to the current permutation
            set the position of this in the used array to True to signalits been processed
            recurse the function, but increse the depth

  '''
  permutations.append(current_permutation[::]) # use deepcopy because current_permutation is tracking all partial solution, it eventually becomes []
  
  for i in range(n): # go over every variable in ever recursive call
    print(i)
    print(used)
    if not used[i]: # If the used array that tracks whats been used in the recursive call for this iteration of n hasent been done
      current_permutation.append(a[i]) # To the current permutation array, append the data at the current postision to the array we're in
      used[i] = True # For this current iteration 
      print(current_permutation)
      # move to the next solution
      permutation_maker(a, n, depth+1, used, current_permutation, permutations)
      
      # When the recursion has finished
      current_permutation.pop()
      print('backtrack: ', current_permutation)
      used[i] = False
  return

if __name__ =="__main__":

    a = [1, 2,]
    n = len(a)
    # Used is a list that will track wether or not
    used = [False] * len(a)
    ans = []
    all_possible_permutation_array(a, n, k, 0, used, [], ans)
    print(ans)