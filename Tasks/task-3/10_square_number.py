number = int(input('Enter the number: '))
if number > 10:
    print('Number is not less than 10.')
elif number == 10:
    print('Number is a 10.')
else:
    print(f'Square of {number} is a {number*number}')