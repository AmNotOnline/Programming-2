# Write your code here
def includes(xs: list[int], ys: list[int]):
    return set(ys).issubset(set(xs))