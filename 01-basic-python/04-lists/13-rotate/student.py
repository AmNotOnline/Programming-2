# Write your code here
def rotate(xs: list, n: int):
    t = xs[n:] + xs[:n]
    for i in range(len(t)):
        xs[i] = t[i]