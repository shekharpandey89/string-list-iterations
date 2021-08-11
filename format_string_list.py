# python format_string_list.py

'''
 Iterate the string list and formatting it
'''

str_list = ["New York","Los Angeles","Chicago","Houston","Phoenix",
            "Philadelphia"]


for i, word in enumerate(str_list):
    print ("string[{}] = {}".format(i, word))