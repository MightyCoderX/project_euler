"""
<p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
<p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>
"""

def largest_palindrome_product():
    n1 = 999
    palindromes = []
    while True:
        for n in range(999, 100, -1):
            result = n1*n
            if str(result) == "".join(reversed(str(result))):
                palindromes.append(result)
        if n1 == 100:
            break
        n1-=1
    return max(palindromes)

def main():
    largest = largest_palindrome_product()
    print(largest) # 906609

if __name__ == '__main__':
    main()