from math import sqrt, floor

def sum_primes_below(limit):
    prime_candidate = 2
    sum = 0
    while prime_candidate < limit:
        is_prime = True
        end = floor(sqrt(prime_candidate)) + 1
        for div in range(2, end):
            if prime_candidate % div == 0:
                is_prime = False
                break
        
        if is_prime:
            sum += prime_candidate
        
        prime_candidate += 1
    
    return sum


def main():
    print(sum_primes_below(2e6))

if __name__ == '__main__':
    main()