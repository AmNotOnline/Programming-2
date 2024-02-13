# Write your code here
def digit_sum(n: int):
    s = 0
    while n != 0:
        s += last_digit(n)
        n = remove_last_digit(n)
    return s

def last_digit(n: int):
    return n % 10

def remove_last_digit(n: int):
    return n // 10

print(digit_sum(11323))