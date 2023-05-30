'''
Q11. Something fishy there -
Find output of following:
def f(x,l=[]):
for i in range(x):
l.append(i*i)
print(l)
f(2)
f(3,[3,2,1])
f(3)
'''

#Q1
'''
Output for f(2): [0, 1]
Explanation: The first function call f(2) initializes the list l as an empty list []. 
It appends the squares of 0 and 1 to the list l using the append method. 
The resulting list is [0, 1], which is then printed.
'''

#Q2

'''
Output for f(3, [3, 2, 1]): [3, 2, 1, 0, 1, 4]
Explanation: The second function call f(3, [3, 2, 1]) passes a different list [3, 2, 1] as the argument l. 
The function appends the squares of 0, 1, and 2 to this list. 
The resulting list is [3, 2, 1, 0, 1, 4], which is then printed.
'''

#Q3

'''
Output for f(3): [0, 1, 4, 0, 1, 4]
Explanation: The third function call f(3) does not pass any value for l, so the default value [] is used. 
It appends the squares of 0, 1, and 2 to the existing list l, resulting in [0, 1, 4]. 
This modified list is then printed.
'''