# write a function of 3 arguments all strings
# function should return lexigraphically ordered string of unique characters
# these unique characters must be present in BOTH  of the first two strings 
# BUT not in the third "badstring"

# example:
# "abcf", "fab", "boo"  returns -> "af" 
# because "a" is in both "abc" and "fab" but not in "boo"
# same goes for "f" it is present in both "good strings" but not in "badstring"
# notice "b" is not in the result because it is in the badstring.

# slightly harder way would be to use loops and if statements to check each character
# the easy way is to use sets and set operations 😊

# either approach is acceptable

 ## 1.One-liner with list

def ordered_string(seq1, seq2, seq3):
    
    return [i for i in seq1 if i in seq2 and i not in seq3]
    
## 2 String  

def ordered_string(seq1, seq2, seq3):
    empty_string = ''
    my_list = [i for i in seq1 if i in seq2 and i not in seq3]
    empty_string = ''.join(my_list)
    return empty_string

### Set operations

def ordered_string(seq1, seq2, seq3):
    return (set(seq1) & set(seq2)) - set(seq3)

my_string = ordered_string('abcf', 'fab', 'boo')
print(my_string)