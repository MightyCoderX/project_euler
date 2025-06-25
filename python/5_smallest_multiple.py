"""
<p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
<p>What is the smallest positive number that is <strong class="tooltip">evenly divisible<span class="tooltiptext">divisible with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>
"""

def smallest_multiple():
    n = 2

    divisible = False
    while not divisible:
        all_div = True
        for div in range(1, 20 + 1):
            if n % div != 0:
                all_div = False
                break
        
        divisible = all_div

        n += 1

    return n-1

def main():
    print(smallest_multiple()) # 

if __name__ == '__main__':
    main()