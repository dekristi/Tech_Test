#1. The Big Result

# Write an add_mult function that requires three parameters / arguments

# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.

# PS Assume that numeric parameters will always be passed to the function, no need to check types

# Various solutions are possible (you are allowed to use other data structures inside function such as list).

# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30

# PSS function should return the result, not print it.

def add_mult(a: int, b: int, c: int):
    my_list = [a,b,c]
    sort_list = sorted(my_list)
    a = sort_list[0]
    b = sort_list[1]
    c = sort_list[2]
    result = (a + b) * c
    return result

my_result = add_mult(5,2,4)
print(my_result)