'''
Q3. Column Sorting, yay
Given a list of dicts, write a program to sort the list according to a key given in input.
E.g.
Input f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "fruit")
Should Output
[
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"},
{"fruit": "orange", "color": "orange"}
]
AND
Input f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "color")
Should Output
[
{"fruit": "blueberry", "color": "blue"},
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"}
]
'''
def sort_list_of_dicts(list_of_dicts, sort_key):
    return sorted(list_of_dicts, key=lambda x: x.get(sort_key))


list_of_dicts = []

list_of_dicts = []
while True:
    dictionary = {}
    dict_input = input("Enter yes or no to add dictionary in list: ")
    if dict_input == "no":
        break

    while True:
        print("Enter details for a key (or enter 'stop' to finish):")
        key = input("Enter key: ")
        if key == "stop":
            break
        value = input("Enter value: ")
        dictionary[key] = value
    list_of_dicts.append(dictionary)


sort_key = input("Enter the key to sort the list of dictionaries: ")

sorted_list = sort_list_of_dicts(list_of_dicts, sort_key)

print("Sorted list of dictionaries: ")
print(sorted_list)



