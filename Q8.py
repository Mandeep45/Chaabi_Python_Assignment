'''
Q8. Some neat tricks up her sleeve:
Looking at the below code, write down the final values of A0, A1, ...An
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
A8 = map(lambda x: x*2, [1,2,3,4])
A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])

'''

#A0
'''
The value of A0 is a dictionary created by zipping the keys ('a', 'b', 'c', 'd', 'e')
with the corresponding values (1, 2, 3, 4, 5).
Here, The zip function combines the keys and values into pairs.
Final value of A0: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.
'''

#A1
'''
The value of A1 is a range object that represents numbers from 0 to 9.
Final value of A1: range(0, 10)
'''

#A2
'''
The value of A2 is a sorted list comprehension that filters the numbers from A1 
that exist as keys in A0.
Final value of A2: []
'''

#A3
'''
The value of A3 is a sorted list comprehension that 
retrieves the values from A0 based on the keys in A0.
Final answer of A3 = [1, 2, 3, 4, 5].
'''

#A4
'''
The value of A4 is a list comprehension that filters the numbers from A1 
that exist in A3. Since A3 contains all the values from 1 to 5,
Final answer of A4 = [1, 2, 3, 4, 5].
'''

#A5
'''
The value of A5 is a dictionary comprehension that creates key-value pairs 
where the keys are the numbers from A1 and the values are the square of those numbers.
Final answer of A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}.
'''

#A6
'''
The value of A6 is a list comprehension that creates nested lists 
where the first element is the number from A1, 
and the second element is the square of that number. 
Final answer of A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]].
'''

#A7
'''
The value of A7 is the result of applying the lambda function to the list [10, 23, -45, 33] 
using the reduce() function. 
The lambda function adds the elements together.
Final answer of A7 = 21.
'''

#A8
'''
The value of A8 is a map object that applies the lambda function (multiplying each element by 2)
to each element in the list [1, 2, 3, 4].
Note that A8 is a map object and not a list. To see the actual values, 
you can convert it to a list by using list(A8).
Final answer of A8 = [2, 4, 6, 8].
'''

#A9
'''
The value of A9 is a filter object that applies the lambda function (checking the length of each element) to 
each element in the list ["I", "want", "to", "learn", "python"]. 
It filters out the elements that have a length greater than 3.
Note that A9 is a filter object. To see the actual values, 
you can convert it to a list by using list(A9).
Final answer of A9 = ["want", "learn", "python"].
'''