name1 = input('Please enter a text! ').lower()
name2 = input('Please enter a text! ').lower()

count_list = ''

for i in name2:
    if i not in count_list and i in name1[::]:
        count_list += str((i) + " " + str(name1.count(i)) + ",")
        count_list_split = count_list.split(',')
        alphab_list = ', '.join(sorted(count_list_split, key=str.lower))

print(alphab_list)

if i not in count_list:
    print("None of characters are in the first string")