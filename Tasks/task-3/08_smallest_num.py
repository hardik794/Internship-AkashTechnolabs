num1 = int(input('enter number-1:'))
num2 = int(input('enter number-2:'))

if num1 == num2:
    print(f'{num1} and {num2} are equal.')
elif num1 > num2:
    print(f'{num2} is smaller than {num1}.')
else:
    print(f'{num1} is smaller than {num2}.')