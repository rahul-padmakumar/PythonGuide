
def is_palindrome(input_data):
    input_without_space = input_data.replace(" ", "")
    return input_without_space == input_without_space[::-1]


print(is_palindrome("helleh"))
print(is_palindrome("nurses run"))
