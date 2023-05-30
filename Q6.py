'''
Q6. Every other sub-list
Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
contain every second element.
'''

def get_every_other_sublist(lst, start_index, end_index):
    sub_list = lst[start_index:end_index+1]
    every_other_sub_list = sub_list[::2]
    return every_other_sub_list


size = int(input("Number of elements in list1: "))
list1 = [input("Enter element {}: ".format(i + 1)) for i in range(size)]

start_index = int(input("start_index is: "))
end_index = int(input("end_index is: "))

result = get_every_other_sublist(list1, start_index, end_index)
print(result)
