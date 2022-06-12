# put your python code here
input_numbers = []

user_input = int(input())
input_numbers.append(user_input)

while sum(input_numbers) != 0:
    input_numbers.append(int(input()))

squares_numbers = [i ** 2 for i in input_numbers]
print(sum(squares_numbers))