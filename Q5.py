'''
Q5. Common, Not Common
Given 2 lists in input. Write a program to return the elements, which are common to both
lists(set intersection) and those which are not common(set symmetric difference) between the
lists.

'''

def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    not_common_elements = list(set(list1) ^ set(list2))
    return common_elements, not_common_elements

n = int(input("Number of elements in list1: "))
list1 = [input("Enter element {}: ".format(i + 1)) for i in range(n)]

m = int(input("Number of elements in list2: "))
list2 = [input("Enter element {}: ".format(i + 1)) for i in range(m)]

common, not_common = compare_lists(list1, list2)
print("Common elements:", common)
print("Not common elements:", not_common)

