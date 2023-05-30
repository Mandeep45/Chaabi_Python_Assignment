'''
Q1. Get your basics right - Implement selection sort algorithm in python. The function accepts a
list in the input and returns a sorted list.
E.g.
Input f1([5,416,54,21,6135,15,741]) should
Return [5, 15, 21, 54, 416, 741, 6135] 
'''



def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


num = input("Enter list of number separated by commas: ")
num_list = [int(num) for num in num.split(",")]

selection_sort(num_list)

print(num_list)
