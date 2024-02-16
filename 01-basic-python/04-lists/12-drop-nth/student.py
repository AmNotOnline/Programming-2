# Write your code here
def drop_nth(xs: list, n: int):
    return xs[:n] + xs[n+1:]    # List concatenation