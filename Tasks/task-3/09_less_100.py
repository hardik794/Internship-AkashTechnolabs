number = int(input('Enetr the number: '))
if number > 100:
    print('Number is greater than 100.')
elif number == 100:
    print('Number is a 100.')
else:
    if number % 2 == 0:
        print('Number is less than 100 and even.')
    else:
        print('Number is less than 100 and odd.')