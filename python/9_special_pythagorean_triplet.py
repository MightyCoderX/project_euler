"""
<p>A Pythagorean triplet is a set of three natural numbers, $a \\lt b \\lt c$, for which,
$$a^2 + b^2 = c^2.$$</p>
<p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
<p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.</p>
"""

from math import sqrt, ceil

def special_pythagorean_triplet(s):
    # a < b < c (pythagorean triplet)
    # a + b + c = s => c = s - a - b
    for a in range(1, s):
        for b in range(a, s):
            c = s - a - b # calculate c instead of using another loop like i did originally XD
            if a**2 + b**2 == c**2: # pythagorean triplet
                print(a, b, c)
                if a + b + c == s:
                    return a * b * c


def main():
    print(special_pythagorean_triplet(1000))

if __name__ == '__main__':
    main()