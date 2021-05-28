number = int(input('Enter the number: '))
if number >= 0:
    if number == 0:
        print(f"{number} is Zero.")
    else:
        print(f"{number} is Positive.")
else:
    print(f"{number} is Negative.")