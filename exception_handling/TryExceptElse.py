
def ask():
    while True:
        number = input("Please enter a number: ")
        try:
            square = int(number) ** 2
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print('Thank you, your number squared is: {}'.format(square))
            break


ask()