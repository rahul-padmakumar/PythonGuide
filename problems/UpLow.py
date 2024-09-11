
def up_low(data):
    upper_case_letters = 0
    lower_case_letters = 0
    for ch in data:
        if ch.isupper():
            upper_case_letters += 1
        elif ch.islower():
            lower_case_letters += 1
    print("Original String: {}".format(data))
    print("No. of Upper case characters :  {}".format(upper_case_letters))
    print("No. of Lower case Characters :  {}".format(lower_case_letters))


up_low("Hello Mr. Rogers, how are you this fine Tuesday?")