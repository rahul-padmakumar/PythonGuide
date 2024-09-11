import string


def is_pangram(input_data):
    unique_data = set(input_data.replace(" ", ""))
    alphabet_set = set(string.ascii_lowercase)
    return len(alphabet_set - unique_data) == 0


print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello World"))
