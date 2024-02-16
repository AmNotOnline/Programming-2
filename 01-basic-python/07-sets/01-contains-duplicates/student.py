# Write your code here
def contains_duplicates(ns: list):
    return len(ns) != len(set(ns))