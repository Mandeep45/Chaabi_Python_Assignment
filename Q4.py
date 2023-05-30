'''
Q4. The power of one line -
Given a dictionary, switch position of key and values in the dict, i.e., value becomes the key and
key becomes value. The function's body shouldn't have more than one statement.
f({
"key1": "value1",
"key2": "value2",
"key3": "value3",
"key4": "value4",
"key5": "value5"
}) should return
{
"value1": "key1",
"value2": "key2",
"value3": "key3",
"value4": "key4",
"value5": "key5"
}

'''

def switch_dict_keys_values(dictionary):
    return {value: key for key, value in dictionary.items()}

my_dict = {}

while True:
    key = input("Enter a key (or 'done' to finish): ")
    if key == "done":
        break
    value = input("Enter the corresponding value: ")
    my_dict[key] = value

print("Your dictionary:")
print(my_dict)


result = switch_dict_keys_values(my_dict)
print(result)
