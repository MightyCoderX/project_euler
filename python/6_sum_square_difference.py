"""
<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385.$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
"""

def sum_square_difference():
    sum_of_squares = sum([n**2 for n in range(1, 101)])
    
    square_of_sum = sum([n for n in range(1,101)])
    square_of_sum = square_of_sum**2

    return square_of_sum - sum_of_squares

def main():
    print(sum_square_difference())

if __name__ == '__main__':
    main()