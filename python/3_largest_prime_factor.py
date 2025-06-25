"""
<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
<p>What is the largest prime factor of the number $600851475143$?</p>
"""

def largest_prime_factor(n):
    largest = 0
    prod = 1
    prime_factor_candidate = 2
    
    while prod < n:
        is_prime = True
        for div in range(2, prime_factor_candidate):
            if prime_factor_candidate % div == 0:
                is_prime = False

        if is_prime and n % prime_factor_candidate == 0:
            prod *= prime_factor_candidate
            largest = prime_factor_candidate
        
        prime_factor_candidate += 1

    return largest

def main():
    n = 600851475143
    print(largest_prime_factor(n)) # 6857

if __name__ == '__main__':
    main()