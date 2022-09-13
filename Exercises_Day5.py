for i in range(101):
    if i % 5 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)

## Christmas tree

ask = input("Please enter the hight of the tree! ")

height = int(round(float(ask), 0))
stars = 1

for i in range(height + 1):
    print('*')
    while stars < height:
        stars += 2
        print('*' * stars)
    break