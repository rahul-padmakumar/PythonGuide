
def blackjack(a, b, c):
    has_eleven = a == 11 or b == 11 or c == 11
    initial_sum = a + b + c
    final_sum = initial_sum
    if initial_sum > 21 and has_eleven:
        final_sum = initial_sum - 10
    if final_sum > 21:
        return 'BUST'
    else:
        return final_sum


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))