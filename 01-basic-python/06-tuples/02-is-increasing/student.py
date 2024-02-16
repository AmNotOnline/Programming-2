# Write your code here
def is_increasing(ns: list[int]):
    return not any(map(lambda t: t[0] > t[1], zip(ns, ns[1:])))
    