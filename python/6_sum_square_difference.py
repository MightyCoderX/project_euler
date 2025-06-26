"""
<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385.$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
"""

def sum_square_difference(limit):
    sum_of_squares = 0
    sum = 0
    
    for n in range(1, limit+1):
        sum_of_squares += n**2
        sum += n

    return sum**2 - sum_of_squares

def main():
    print(sum_square_difference(100)) # 25_164_150

if __name__ == '__main__':
    main()