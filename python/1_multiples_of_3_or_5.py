"""
<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
"""

def sum_multiples():
    sum = 0
    for n in range(1000):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    
    return sum

def main():
    print(sum_multiples()) # 233168

if __name__ == '__main__':
    main()