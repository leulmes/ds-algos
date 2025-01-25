# collatz conjecture (recursion practice)
def collatz(n):
    # base case
    if n == 1:
        return 0
    # recursive case
    elif (n % 2) == 0:
        return 1 + collatz(n / 2)
    else:
        return 1 + collatz((3*n) + 1)
    
print(collatz(1))
print(collatz(4))
print(collatz(7))
    