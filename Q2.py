'''
Q2. Dictionary, what?
Write a program that returns the file type from a file name. The type of the file is determined
from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
png,image) will be input.
The program takes input in the following form:
1. Input extension and type values in the form of a string having the following format:
a. "extension1,type1;extension2,type2;extension3,type3"
b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
"xyz.xls", "text.csv", "123"]
The program should return a dict of filename: type pairs
E.g.
f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
"xyz.xls", "text.csv", "123"]) should return
{
"abc.jpg": "image",
"xyz.xls": "spreadsheet",
"Text.csv": "unknown",
"123": "unknown"
}

'''
def get_file_type(extension_type_list, filenames):
    extension_type_pairs = [pair.split(",") for pair in extension_type_list.split(";")]
    extension_type_dict = {pair[0]: pair[1] for pair in extension_type_pairs}

    file_type_dict = {}
    for filename in filenames:
        extension = filename.split(".")[-1]
        if extension in extension_type_dict:
            file_type_dict[filename] = extension_type_dict[extension]
        else:
            file_type_dict[filename] = "unknown"

    return file_type_dict


extension_type_list = input("Enter extension and type values: ")
filenames = input("Enter list of filenames: ").split(",")

file_type_dict = get_file_type(extension_type_list, filenames)
print(file_type_dict)
