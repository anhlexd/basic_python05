# 1. Implement the algorithm from description (String: 8-1):
# The program asks the user to enter a string. It then uses a for loop to iterate
# over the string, counting the number of times that the letter T (uppercase or
# lowercase) appears.

str_txt = input('Enter the string: ')
count = 0

for i in str_txt:
    if i == 't' or i == 'T':
        count += 1 

print(f'The number of times that the letter T (uppercase or lowercase) appears: {count}')