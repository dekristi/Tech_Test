prime_list = [2,]
num = int(input('How many prime numbers do you want to display? '))
start_num = 1

while True:
    prime_list_length = len(prime_list) 

    for i in range(2, start_num):
        if start_num % i == 0 and start_num in prime_list:
            # prime_list = [n.replace("start_num", "") for n in prime_list]
            prime_list = prime_list[:-1]

        if start_num % i == 0:
            break
    
        else:
            if start_num not in prime_list:
                prime_list.append(start_num)
    if prime_list_length < num:
        start_num += 1
    if prime_list_length == num:
        print(prime_list)
        break