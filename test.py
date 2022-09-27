# 2. Common Elements
# Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.

# get_common_elements(seq1, seq2, seq3)

# Example:

# get_common_elements("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element 

# # remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)

# 2. b For those with some experience 

# BONUS:  make a function that can handle an arbitrary number of input sequences
# so function which takes any number of sequences and returns a tuple with common elements
# get_common_elements(seq1, seq2, seq3, seq4, seq5, seq6, seq7) etc :), so just like print takes any number of values

def common_elements(seq1, seq2, seq3):
    same_elements = set(seq1) & set(seq2) & set(seq3)
    tup_same_elements = tuple(same_elements)
    return tup_same_elements

my_elements = common_elements(['a', 'b'], ('b', 'c'), "abc")
print(my_elements)

from statistics import mean
def get_min_avg_max (seq: tuple):
    min_num = int(min(seq))
    max_num = int(max(seq))
    avg_num = int(mean(seq))
    my_string = (min_num, avg_num, max_num,)
    return my_string

min_avg_max = get_min_avg_max([0,10,1,9])
print(min_avg_max)