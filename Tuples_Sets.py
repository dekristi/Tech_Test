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
    return set(seq1) & set(seq2) & set(seq3)


my_elements = common_elements(['a', 'b'], ('b', 'c'), "abc")
print(my_elements)

from statistics import mean
def get_min_avg_max (seq: tuple):
    return min(seq), mean(seq), max(seq)

min_avg_max = get_min_avg_max([0,10,1,9])
print(min_avg_max)

# 3. Is there a pangram?

# Write a function is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz')

# that returns True when the text parameter contains all the letters passed in an alphabet.
# We return False otherwise

# pangram - sentence, word string containing all letters of the alphabet - https://en.wikipedia.org/wiki/Pangram

# We ignore spaces and believe that uppercase is as valid as lowercase, i. here A and a -> a

# print(is_pangram("The five boxing wizards jump quickly")) -> True
# print(is_pangram("Not a pangram")) -> False

# Bonus: test it also on Latvian alphabet:
# a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'

# print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', alphabet=a_lv)) -> True

# Bonus: test it also on Lithuanian alphabet:
# a_lt = 'aąbcčdeęėfghiįyjklmnoprsštuųūvzž' # see if this correct

# some languages have perfect pangrams, some do not
# perfect pangram - a pangram that uses every letter of the alphabet at just once

def is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz'):
    spl_text = set(text.lower())
    spl_alph = set(alphabet)
    return spl_alph.issubset(spl_text)

my_text = is_pangram("The five boxing wizards jump quickly", alphabet='abcdefghijklmnopqrstuvwxyz')
print(f'is_pangram {my_text}')