from cgitb import text
from codecs import utf_8_encode
from importlib.resources import path
import os  
from pathlib import Path  
# Exercise
# read text from  sherlock_holmes_adventures.txt
# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file
# check file_line_len("sherlock_holmes_adventures.txt") -> 12305
my_path = Path(r"..\..\SheGoesTech\Python_SheGoesTech_22\Day12_File_Operations\sherlock_holmes_adventures.txt")
# print(my_path)
def file_line_len(file):
    len_count = 0
    with open(file, encoding="utf-8") as fl:
        for _ in fl:
            len_count += 1
    return len_count

# print(file_line_len(my_path))

# 1b -> write the function get_text_lines(fpath), which returns a list with only those lines that contain text.
# So we want to avoid/filter out those lines that contain whitespace

def get_text_lines(file):
    with open(file, encoding="utf_8") as fl:
        clean_text = [line.strip() for line in fl if line.rstrip()]
    return clean_text

my_text = get_text_lines(my_path)
# print(my_text[:10])

# 1c -> write the function save_lines(destpath, lines)
# This function will store all lines into destpath file 
def save_lines(destpath, lines, encoding='utf_8', sep='\n'):
    with open(destpath, mode='w', encoding=encoding) as fl:
        with open(lines, encoding=encoding) as file_out:
            for line in file_out:
                fl.write(line + sep)

save_lines("sherlock_holmes_new.txt", my_path)

# 1d -> call save_lines with destpath being "pure_sherlock.txt" and lines being the text lines we cleaned from 1b
# print(my_text[:20])
# for elem in my_text:
#     new_text = ''.join(elem)
# # 

# #     
# save_lines("pure_sherlock.txt", new_text)

# 1e -> write the function clean_punkts(srcpath, destpath)
# import string
# def clean_punkts(scrpath, destpath):
# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation

# then function will save the cleaned text into destpath
# clean_punkts("pure_sherlock.txt", "clean_sherlock.txt")


# 1f -> write the function get_word_usage(srcpath, destpath)

# The function opens the file and finds the most frequently used words

# recommendation to use Counter module!

# assume that the words are separated by either whitespace or newline (the good old split will come in handy)

# the saved list of words and frequency should be saved in destpath in the following form:

# word, count
# un, 3423
# es, 3242

# in effect you will be saving in standard csv format - https://docs.python.org/3/library/csv.html
# you can use csv module for this, but it is not necessary