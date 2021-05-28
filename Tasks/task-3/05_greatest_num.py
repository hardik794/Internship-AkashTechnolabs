num1 = int(input('enter number-1:'))
num2 = int(input('enter number-2:'))

if num1 == num2:
    print(f'{num1} and {num2} are equal.')
elif num1 > num2:
    print(f'{num1} is greater than {num2}.')
else:
    print(f'{num2} is greater than {num1}.')