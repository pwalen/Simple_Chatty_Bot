input_list = []

while True:
    user_input = input()
    if user_input != 'MEOW':
        input_list.append(user_input)
    else:
        break

list_of_lists = []
for x in input_list:
    list_of_lists.append(x.split(" "))

names = []
numbers = []

for x in list_of_lists:
    names.append(x[0])
    numbers.append(int(x[1]))

max_num = max(numbers)
max_num_index = numbers.index(max_num)

print(names[max_num_index])
