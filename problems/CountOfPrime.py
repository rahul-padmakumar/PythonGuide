

def is_prime(number):
    div_count = 0
    for i in range(2, number):
        if number % i == 0:
            div_count += 1
    return div_count == 0


def count_primes(limit):
    count = 0
    for i in range(2, limit):
        if is_prime(i):
            count += 1
    return count


print(count_primes(100))

