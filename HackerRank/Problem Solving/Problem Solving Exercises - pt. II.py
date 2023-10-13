import math
import itertools


'Encryption'

# My Approach

# s = 'ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots'
# # print(len(s))

# columns = math.ceil(math.sqrt(len(s)))
# # print(f'ceil: {columns}')

# rows = math.floor(math.sqrt(len(s)))
# # print(f'floor: {rows}')

# if rows * columns < len(s):
#     rows = columns

# result, rows_words = list(), list()

# for i in range(rows):
#     rows_words.append(s[i*columns:i*columns+columns])
    
# # print(rows_words)

# for i in range(columns):

#     temp = str()

#     for j in rows_words:

#         if i > len(j)-1:
#             continue
        
#         temp += j[i]
    
#     result.append(temp)

# # print(result)

# result_string = str()

# for i in result:    
#     result_string += i + ' '

# result_string.rstrip()

# print(result_string)


'''
This solution is the first draft that came to mind but I'm sure it could be a lot more efficient,
Below there is a solution that came from ChatGPT
'''

# def encryption(s):

#     s = s.replace(" ", "")  # Remove spaces
#     L = len(s)
#     R = int(math.floor(math.sqrt(L)))
#     C = int(math.ceil(math.sqrt(L)))
    
#     while R * C < L:
#         R += 1

#     grid = [['' for _ in range(C)] for _ in range(R)]

#     for i in range(L):
#         row = i // C
#         col = i % C
#         grid[row][col] = s[i]

#     encrypted_message = ""
#     for col in range(C):
#         for row in range(R):
#             if grid[row][col] != '':
#                 encrypted_message += grid[row][col]
#         encrypted_message += " "  # Add space between columns

#     return encrypted_message

# # Example usage:
# input_string = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
# result = encryption(input_string)
# print(result)




'Bigger is Greater'


# w = 'dkhc'


# # Base solution
# comb = list(map(list, itertools.permutations(w)))
# comb = list(map(''.join,comb))

# comb.sort(reverse=True)
# ind = comb.index(w)
# result = comb[ind-1]

# print(comb)
# print(len(comb))
# print(result)


# # Solution sent to HackerRank
# def biggerIsGreater(w):
    
#     comb = list(map(list,itertools.permutations(w)))
#     comb = list(map(''.join,comb))
#     comb.sort(reverse=True)
#     ind = comb.index(w)
#     result = comb[ind-1]
    
#     if ind == 0 or result == w:
#         return 'no answer'
    
#     return result

''' 
This solution evidently is based on brute force,
3 out of the 5 cases failed due to time limit excedeed or runtime error,

    Pending: needs optimization.
'''


# ChatGPT's Solution

'''
According to ChatGPT here, the optimal solution which will be O(n), is to find the inmediate next permutation bigger
by finding the first pair (a,b) where a > b within the characters in the string, then find the rightmost character (c) which satisfies c > a, and then
swap those two and reverse that part of the string
'''

# def biggerIsGreater(w):
    
#     w = list(w)

#     i = len(w) - 2

#     while i >= 0 and w[i] >= w[i + 1]:
#         i -= 1

#     if i == -1:
#         return 'no answer'    


#     j = len(w) - 1

#     while w[j] <= w[i]:
#         j -= 1

#     w[i], w[j] = w[j], w[i]


#     w[i + 1:] = reversed(w[i + 1:])

#     return ''.join(w)

# print(biggerIsGreater(w))

'''
Done!
'''




'Modified Kaprekar Numbers'


# # My Solution
# p = 1
# q = 100

# rang = range(p,q+1)

# kapr_nums = list()

# for i in rang:

#     d = len(str(i))

#     pow2 = pow(i,2)
#     pow2 = str(pow2)
#     r = pow2[-d:]
#     l = pow2[:-d]

#     if l != '':
#         l,r = int(l),int(r) 
    
#     else:
#         l,r = 0, int(r)

#     if r + l == i:
#         kapr_nums.append(i)
        
# print(kapr_nums)


'''
My solution worked just fine, but I am curious if there was another way to do it without brut forcing it

    Note: After reviewing the discussion board and ChatGPTs opinion, all the solutions converge in the same solution.
'''




'Beutiful triplets'


# arr = [1, 2, 4, 5, 7, 8, 10]
# arr = [2,2,3,4,5]
# d = 3

# # First approach
# triplets = list(itertools.combinations(arr,3))

# b_triplets = list()

# for i in triplets:

#     if i[2] - i[1] == i[1] - i[0] == 3:
#         b_triplets.append(i)

# print(b_triplets)

'Brute forcing it wont do, Ill try somehting different'


# # Second approach
# b_triplets = list()

# for i in range(len(arr) - 2):

#     triplet = list()
#     triplet.append(arr[i])
    
#     for j in range(i+1, (len(arr)-2) + 1):

#         if arr[j] - arr[i] == d:
#             triplet.append(arr[j])

#             for k in range(j+1, len(arr)):

#                 if arr[k] - arr[j] == d:

#                     triplet.append(arr[k])
#                     b_triplets.append(triplet)
#                     triplet = triplet[:-1]
            
#             triplet = triplet[:-1]
  
# print(b_triplets)

'This second approach worked perfectly'




'Minimum Distances'


# # My Approach
# a = [3,2,1,2,3]
# a = [7, 1, 3, 4, 1, 7]

# distances = list()

# for ind, elem in enumerate(a):  

#     if a.count(elem) <= 1:
#         continue

#     for j in range(ind+1, len(a[ind+1:]) + 1):

#         if a[j] == elem:            
#             distances.append(abs(j-ind))

# distances.sort()

# print(distances)
# print(distances[0])

'''
When submitting my solution to HR, it worked 80% of the time
But after checking with ChtaGPT, there a couple of problems with my solution
to begin with it has a compl of O(n^2) and there is time when pairing are ignored
due to the 'range(ind+1, len(a[ind+1:]) + 1)' loop, 
and the final sorting adds another complexity of O(n log n), which, apparently is unnecessary

There's another approach based on dict that works more efficiently
'''

# a = [7, 1, 3, 4, 1, 7]


# def minimumDistance(a):

#     element_to_index = dict()
#     min_distance = float('inf')


#     for i, elem in enumerate(a):

#         if elem in element_to_index:

#             distance = i - element_to_index[elem]
#             min_distance = min(distance, min_distance)

#         element_to_index[elem] = i

#     return min_distance if min_distance != float('inf') else -1


# print(minimumDistance(a))


'This solution has a compl of O(n) and works 100% of times'




'Halloween Sale'

# inp = [int(x) for x in '100 19 1 180'.split()]

# p = inp[0]
# d = inp[1]
# m = inp[2]
# s = inp[3]

# count = int()

# if s >= p:

#     while s >= m and s >= p:

#         count += 1

#         if p > m:       
#             s -= p
#             p -= d

#         else:
#             s -= m

# else:
#     count = 0

'This solution worked just fine'




'The Time in Words'


# words = [
#     'one',
#     'two', 
#     'three', 
#     'four', 
#     'five', 
#     'six', 
#     'seven', 
#     'eight', 
#     'nine', 
#     'ten', 
#     'eleven', 
#     'twelve', 
#     'thirteen', 
#     'fourteen', 
#     'quarter', 
#     'sixteen', 
#     'seventeen', 
#     'eighteen', 
#     'nineteen', 
#     'twenty', 
#     'twenty one', 
#     'twenty two', 
#     'twenty three', 
#     'twenty four', 
#     'twenty five', 
#     'twenty six', 
#     'twenty seven', 
#     'twenty eight', 
#     'twenty nine', 
#     'half'
#     ]

# numbers = range(1,31)

# time_in_words = list(zip(numbers,words))

# dict_time = {k:v for k,v in time_in_words}


# h = 7
# m = 15

# if m == 0:
#     print(f"{dict_time[h]} o' clock")

# elif m == 1:
#     print(f"{dict_time[m]} minute past {dict_time[h]}")

# elif m == 15:
#     print(f"quarter past {dict_time[h]}")

# elif m == 30:
#     print(f"half past {dict_time[h]}")

# elif m > 30 and m != 45 and m != 59:
#     print(f"{dict_time[60-m]} minutes to {dict_time[h+1]}")

# elif m == 45:
#     print(f"quarter to {dict_time[h+1]}")

# elif m == 59:
#     print(f"one minute to {dict_time[h+1]}")

# else:
#     print(f"{dict_time[m]} minutes past {dict_time[h]}")


'Done!'




'Chocolate Feast'

# n = 15
# c = 3
# m = 2

# wrappers = int()
# chocolates = int()

# wrappers = chocolates = n // c

# while True:

#     chocolates += wrappers // m
#     wrappers = (wrappers // m) + (wrappers % m)

#     if wrappers < m:
#         break
    

# print(chocolates)

'Done!'




'Service Lane'

# width = [2, 3, 1, 2, 3, 2, 3, 3]
# cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]

# result = list()

# for case in cases:
#     result.append(min(width[case[0]:case[1]+1]))

# print(result)

'Done!'




"Lisa's Workbook"

# # Input
# n = 1
# k = 1
# arr = 100


# # My Approach
# page = 1
# workbook = list()
# special_problems = int()

# if type(arr) is int:
#     arr = [arr]

# for chapter in range(len(arr)):

#     problems_in_page = list()

#     for i in range(1, (math.ceil(arr[chapter]/k)*k)+1):
        
#         if i > arr[chapter]:
#             break

#         problems_in_page.append(i)

#         if len(problems_in_page) == k or i == arr[chapter]:         

#             workbook.append([page, problems_in_page.copy()])
#             page += 1            
#             problems_in_page.clear()
              

# for i in range(len(workbook)):

#     if workbook[i][0] in workbook[i][1]:

#         special_problems += 1
    

# print(workbook)
# print(special_problems)


'''
This solution worked, but seems little to forced. I am gonna check if there is something more sophisticated.

    There actually was but the logic was the same, there was a listcomp. to abreviate the separation of pages by chapter

    for problems_in_chapter in arr:
        chapter = [j for j in range(1, problems_in_chapter + 1)]
        chapter_splitted = [chapter[n : n + k] for n in range(0, len(chapter), k)]

but at the core, the solution was the same.

'''




"Flatland Space Stations"

# # Input
# n = 5
# c = [0, 4]


# # My approach
# cities = [city for city in range(n)]

# cities_with_nearest_st = list()
# max_distance = 0


# for city in cities:
    
#     dist_to_st = [abs(city - c[st]) for st in range(len(c))]

#     cities_with_nearest_st.append([city, min(dist_to_st)])



# for i in cities_with_nearest_st:

#     max_distance = max(max_distance, i[1])


# print(max_distance)


'My solution pass 19/20 cases and the one that didnt passed was due to time limit'


# # My second try
# cities = list(range(n))

# max_distance = 0

# for city in cities:
    
#     dist_to_st = [abs(city - c[st]) for st in range(len(c))]
#     max_distance = max(max_distance, min(dist_to_st))


# print(max_distance)

'After refactoring and cutting one loop, theres still not efficient enough'



# # ChatGPTs Solution

# def flatlandSpaceStations(n, c):

#     # Sort the list of space station locations
#     c.sort()
    
#     max_distance = 0
    
#     # Handle the first city to the first space station
#     max_distance = c[0]
    
#     # Handle the last city to the last space station
#     max_distance = max(max_distance, n - 1 - c[-1])
    
#     # Calculate the maximum distance between two adjacent space stations
#     for i in range(1, len(c)):
#         distance = (c[i] - c[i-1]) // 2
#         max_distance = max(max_distance, distance)
    
#     return max_distance

# print(flatlandSpaceStations(n, c))




"Fair Rations"

# B = [2, 3, 4, 5, 6]
# # B = [4,5,6,7]
# # B = [5,6,8,7]

# odds = [x for x in B if x%2 != 0]
# loaves = int()

# # print(odds)


# if len(odds)%2 != 0:
#     print('NO')
    

# else:
#     for i in range(len(B)):

#         if B[i]%2 == 0:
#             continue

#         else:            
#             B[i] += 1 
#             B[i+1] += 1
#             loaves += 2


# print(loaves)

'This one went smoothly, Done!'




"Cavity Map"        

# grid = ['1112', '1912', '1892', '1234']

# # 1 1 1 2
# # 1 9 1 2
# # 1 8 9 2
# # 1 2 3 4

# grid = [[int(x) for x in elem] for elem in grid]
# cavities = list()

# for row in range(1, len(grid)-1):

#     for col in range(1, len(grid[row])-1):

#         cell = grid[row][col]
#         group = (grid[row][col-1], grid[row][col+1], grid[row-1][col], grid[row+1][col])
        
#         if 'X' not in group and cell > max(group):
#             grid[row][col] = 'X'

#         else:
#             continue

# grid = [''.join(str(x) for x in row) for row in grid]

# for i in grid:
#     print(i)

'This one also went smoothly, Done!'




"Manasa and Stones"

# n = 3
# a = 1
# b = 2

# possibilities = list(itertools.combinations_with_replacement((a,b),r=n-1))

# print(possibilities)
# print()

# possibilities = sorted(map(sum, possibilities))

# result = []

# [result.append(x) for x in possibilities if x not in result]

# print(result)
# print()

'Done!'




"The Grid Search"



# My approach:
def index_caller(li, val):

    occur = list()

    try:
        while True:
            index = li.index(val)
            occur.append(index)
            li = li[index+1:]
    
    except ValueError:
        pass

    return occur


G = ['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137']
P = ['9505', '3845', '3530']


# 7 2 8 3 4 5 5 8 6 4
# 6 7 3 1 1 5 8 6 1 9
# 8 9 8 8 2 4 2 6 4 3
# 3 8 3 0 5 8 9 3 2 4
# 2 2 2 9 5 0 5 8 1 3
# 5 6 3 3 8 4 5 3 7 4
# 6 4 7 3 5 3 0 2 9 3
# 7 0 5 3 1 0 6 6 0 1
# 0 8 3 4 2 8 2 9 5 6
# 4 6 0 7 9 2 4 1 3 7
G = [ [int(x) for x in elem] for elem in G ]

# 9 5 0 5
# 3 8 4 5
# 3 5 3 0
P = [ [int(x) for x in elem] for elem in P ]

res = 'NO'

for i in range(len(G)-len(P) + 1):    
            
    if P[0][0] in G[i][: len(G[0])-len(P[0]) + 1 ]:

        occur = [i for i,v in enumerate(G[i][: len(G[0])-len(P[0]) + 1 ]) if v == P[0][0]]
        # occur = index_caller(G[i][: len(G[0])-len(P[0]) + 1 ], P[0][0] )

        for j in occur:

            sample = [G[i+x][j:j+len(P[0])] for x in range(len(P))]

            if sample == P:
                print('Found It!')
                break


'''
    While I thought my solution without the auxiliary function 'index_caller' may be a good idea
    turns out, my first solution with the indexes called by a listcomp was better, actually worked 94% of times
    and the other 6% was due to time exceeding the limits, so to go on, optimizations must be made:

        - I would start by checking if there's anything better than the two comprehensions at the begining.
'''







# '-xxx- HackerRank Problem Solving Challenge done'
































