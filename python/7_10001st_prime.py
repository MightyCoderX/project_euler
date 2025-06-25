"""
<p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.</p>
<p>What is the $10,001$st prime number?</p>
"""
from math import sqrt, floor

def nth_prime(limit):
    count = 1
    prime_candidate = 1
    while count < limit:
        prime_candidate += 2 # why do I get a +2 in the candidate if I start from 3 and put this at the end of the loop?

        end = floor(sqrt(prime_candidate) + 1)
        is_prime = True
        for div in range(2, end):
            if prime_candidate % div == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

    return prime_candidate

def main():
    print(nth_prime(10_001))

if __name__ == '__main__':
    main()