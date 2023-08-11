from timeit import default_timer as timer


''' Prime numbers' sieve '''

# def primeNumbers (cap):

#     primes, non_primes  = [1], list()

#     for i in range(2, cap + 1):

#         if i not in non_primes:     
            
#             primes.append(i)

#             for j in range( i*i , cap + 1, i):    non_primes.append(j)

#     return primes 

# prime_test = primeNumbers(30)

# print(prime_test)





''' Using eval() To evaluate something for each element of a list '''


# li = [1, 3, 5, 7, 11]
	
# cap = max(li)


# def isPrime (n, cap):   

#     primes, non_primes  = [1], list()

#     for i in range(2, cap + 1):

#         if i not in non_primes:     
            
#             primes.append(i)

#             for j in range( i*i , cap + 1, i):    non_primes.append(j)

#     if n in primes: return True

#     else: return False

# print( ( [ eval( f'isPrime({i},{cap})') for i in li ] ) )   #This shows the eval on each element of the list

# print( all( [ eval( f'isPrime({i},{cap})') for i in li ] ) ) #This line here, tells if every element in the list is a prime number





''' Ordering a dict by values '''


# dict1 = {'A': 100, 'B': 550, 'C': 948, 'D': 95, 'E': 12}

# sorted_dict = { k: v for k, v in sorted( dict1.items(), key = lambda x: x[1], reverse = False ) } # Ascending Order

# print(sorted_dict)





''' Flattening an Array with ListComp '''

# vec = [[1,2,3], [4,5,6], [7,8,9]]
	
# new_list = [num for elem in vec for num in elem]
	
# print(new_list)





''' Transposing a matrix with ListComp & zip( ) functions '''

 
# matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]


# # ListComp
# transp_matrix = [ [ elem[i] for elem in matrix] for i in range(len(matrix[0])) ]

# print(transp_matrix)


# # Using Zip()
# transp_matrix = list( map( list, zip(*matrix) ) )

# print(transp_matrix)



''' ---------- '''


# Most basic loop way to do it
# transp_matrix = [  ]

# for i in range(len(matrix[0])):

#     temp = list()

#     for j in range(len(matrix)):

#         temp.append(matrix[j][i])

#     transp_matrix.append(temp)

# print(transp_matrix)





''' Creating multiple lists quickly '''

# n = 3

# lists = { f'list {i}' : list() for i in range(1, n + 1)   }

# print(lists)





''' Base sorting algorythm '''

# import random


# # Initialize array     
# arr = [random.randint(0,11) for x in range(10)] 

# # Displaying elements of original array    
# # print(f'Elements of the original array: {arr}')    

# s = timer()  

# #Sort the array in ascending order    
# for i in range( len(arr) ): 

#     for j in range( i + 1, len(arr) ): 

#         if(arr[i] > arr[j]):  # '>' will set an asceding order and '<' will set descending 

#             arr[i], arr[j] = arr[j], arr[i]

# e = timer()     

# # Displaying elements of the array after sorting        
# # print(f'Elements of array sorted in ascending order: {arr}', e-s )

# print(e-s)


''' My version of the algorythm without double iteration '''

# import random

# arr = [9, 1, 10, 8, 9, 9, 8, 7, 1, 9] 


# print(f'Array before sortring {arr}')

# for i in range( len(arr) - 1 ):

#     li = arr[ i - len(arr) : ]

#     index = li.index( min( li )) + i

#     if arr[i] > arr[ index ]:  
        
#         arr[i], arr[ index ] = arr[ index ], arr[i]

      
# print(f'Array after sortring {arr}')





''' Taking unique values from a list of dicts '''

# base = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

# base = { v for item in base for v in item.values() }

# print(base)






''' Combining elements of a list of lists without considering order '''

# # First, just as test let's try to combine with regular number of items

# # Initilizing the base list:
    
#     # [3]x[Ir] / [['a', 'b'], ['g'], ['i', 'j']]
#     # [3]x[2] /  [['a', 'b'], ['c', 'd'], ['e', 'f']]
#     # [3]x[3] /  [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]



# base = [['a', 'b'], ['g'], ['i', 'j']]


# # This will be the combinations container
# comb = list()


# # The looping solution would be:

# s = timer()


# for i in range( len(base) -1 ):

#     for j in range( len(base[i]) ): 

#         for k in range( i+1, len(base) ):
            
#             for l in range( len(base[k]) ):

#                 comb.append(f'{base[i][j]}{base[k][l]}')

# e = timer()

# print(comb, (e-s))

'This solution showed to be working just fine'



'----------'

# # This is a Listcomp solution for the same problem


# # Initilizing the base list:
    
#     # [3]x[Ir] / [['a', 'b'], ['g'], ['i', 'j']]
#     # [3]x[2] /  [['a', 'b'], ['c', 'd'], ['e', 'f']]
#     # [3]x[3] /  [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]



# base = [['a', 'b'], ['g'], ['i', 'j']]

# comb = list()

# s = timer()

# for i in range( len(base) - 1 ):

#     for j in range( len( base[i] )):

#         temp_list = [ f'{base[i][j]}{x}' for x in [ x for elem in base[ i + 1: ] for x in elem ] ] 

#         comb.extend(temp_list)

# e = timer()

# print(comb, (e-s))

'This solution also works but showed to be less efficient than the nested for loops one'







''' Combining the elements of a list of lists considering order  '''


# # Initilizing the base list:

#     # [3]x[2] / [['a', 'b'], ['c', 'd'], ['e', 'f']]
#     # [3]x[3] / [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]



# base = [['a', 'b'], ['c', 'd'], ['e', 'f']]


# # This will be the combinations container
# comb = list()

# s = timer()

# for i in range(len(base)):

#     for j in range(len(base[i])):

#         for k in range(len(base)):

#             if k == i:

#                 continue

#             else:

#                 for l in range(len(base[k])):
                    
#                     comb.append( f'{base[i][j]}{base[k][l]}' )

# e = timer()

# print( comb, (e-s) )

'This solution showed to be working just fine'




'----------'

# # This is a Listcomp solution for the same problem


# # Initilizing the base list:

#     # [3]x[2] / [['a', 'b'], ['c', 'd'], ['e', 'f']]
#     # [3]x[3] / [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]


# base = [['a', 'b'], ['c', 'd'], ['e', 'f']]

# comb = list()

# s = timer()

# for i in base:

#     for j in i:

#         temp_list = [f'{j}{x}' for x in [x for elem in base[:base.index(i)] + base[base.index(i)+1:] for x in elem] ]

#         comb.extend(temp_list)

# e = timer()
       
# print(comb, (e-s))


'This solution also works but showed to be less efficient than the nested for loops one'





'''
The first recursion problem I review:

    54. Write a Python program to get the depth of a dictionary.

        Expected Output: 4
    
'''

# d = {'a':1, 'b': {'c': {'d': {}}}}

# def dict_depth(d):

#     if isinstance(d, dict):

#         return 1 + (  max( map ( dict_depth, d.values() ) ) if d else 0 )       # is not that clear to my why it work only with the max() function.
    
#     return 0

# print(dict_depth(d))





'''A Fibonacci Generator'''

# def fibonacci_nums(x=0, y=1):

#     yield x

#     while True:

#         yield y

#         x, y = y, x + y





'''Merging dictionaries'''


'To sum up the |= operator does the sames as the dict.update() function'

# user_base_data = {

#     'name' : 'xxxxx',
#     'last_name' : 'xxxxx',
#     'phone' : 'xxxxxx',
#     'address' : 'xxxx'

# }


# george_data = {

#     'name' : 'George',
#     'last_name' : 'Smith',
#     'phone' : '555-55-55',
   
# }


# user_base_data |= george_data

# print(user_base_data)



# user_base_data.update(george_data)

# print(user_base_data)'''A Fibonacci Generator'''

# def fibonacci_nums(x=0, y=1):

#     yield x

#     while True:

#         yield y

#         x, y = y, x + y





'''Sorting with 2 criteria'''

# # The goal is to pick the three most reppeated letters and also in alphabetical order

# # First will be sorted by occurrence and the alphabetically

# s = 'aaeebbbccd'

# d = { c : s.count(c) for c in s }

# print(d)    # {'a': 2, 'b': 3, 'c': 2, 'd': 1, 'e': 1}


# d = sorted(d.items(), key = lambda x: x[1], reverse = True)

# print(d)    # [('b', 3), ('a', 2), ('e', 2), ('c', 2), ('d', 1)]

# print(d[:3])    # [('b', 3), ('a', 2), ('e', 2)]
# # Here there is the problem: 'a', 'e' and 'c' have the same ocurrences and if we pick the top three just like that,
# # 'c' would be cut out, giving that 'e' should not make the cut instead of 'c'


# 'Here is the solution: the key kwarg give the chance to pass a tuple to consider two criterias at the same time'
# d = sorted(d.items(), key = lambda x: (x[1], x[0]) , reverse = True)

# print(d)    # [('b', 3), ('e', 2), ('c', 2), ('a', 2), ('d', 1)]
# # But the thing is that as reverse kwarg is set in True, it also affects the second criteria x[0], so it returns alphabetically second to ocurrence
# # but, in ascending order, and we need it in descending order 


# # if we try just to set reverse to False, the problem is that also affects the criteria x[1]
# d = sorted(d.items(), key = lambda x: (x[1], x[0]) , reverse = False)

# print(d)    # [('d', 1), ('a', 2), ('c', 2), ('e', 2), ('b', 3)]

# # So to overcome this issue, the solution is to change the occurrence criteria from x[1] to -x[1], that will make it be descending without the reverse kwarg


# d = sorted(d.items(), key = lambda x: (-x[1], x[0]))

# print(d)    # [('b', 3), ('a', 2), ('c', 2), ('e', 2), ('d', 1)]


# 'Solving definitively the problem in case'

# print(d[:3])    # [('b', 3), ('a', 2), ('c', 2)]






''' Unknown number of inputs for a HackerRank problem '''

'''

    Task

    Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
    You will then be given an unknown number of names to query your phone book for. 
    For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
    if an entry for  is not found, print Not found instead.


    input

    ... After the  lines of phone book entries, there are an unknown number of lines of queries. 
    Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.


'''


# N = int(input().strip())

# d = dict()

# for i in range(N):

#     inp = input().strip().split()

#     d[inp[0]] = inp[1]



# while True:

#     try:

#         name = input().strip()

#         inp = d.get(name,'Not found')

#         if inp == 'Not found':
#             print(inp)
        
#         else:
#             print(f'{name}={d[name]}')

#     except EOFError:
#         break




# _ = 'How to create all possible substrings from a string'


# s = 'abcd'

# subs = list()

# #[1,2,3,4]
# for i in range(1, len(s)+1):

#     # R/ 4:[0,1,2,3] ; 3: 
#     for j in range( (len(s)+1) - i ):

#         subs.append(s[j:j+i])


# print(subs) # R/ ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']







_ = 'This is a Index Handler (made by me) to deal with indexes while working with DataStructures '

# def _index_handler(self, index):

#     if self.is_empty():
#         return

#     if index > (self.len()-1) or index < -self.len():
#         raise IndexError('Index out of range')
    
#     # converting the index into a positive index
#     if index < 0: 

#         norm_index = range(self.len())
#         inv_index = range(-len(norm_index),0)
#         dict_index = {k:v for k,v in zip(inv_index, norm_index)}

#         return dict_index[index]

#     else:

#         return index   