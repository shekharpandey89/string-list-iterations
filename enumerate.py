# python enumerate.py

'''
 Iterate the string list using enumerate
'''

str_list = ["New York","Los Angeles","Chicago","Houston","Phoenix",
            "Philadelphia"]

# this will print elements along with their index value
for idx, word in enumerate(str_list):
    print(idx, word)