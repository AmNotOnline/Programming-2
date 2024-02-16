# Write your code here
def contains_duplicates(xs):
    unq = set()
    for item in xs:
        if item not in unq:
            unq.add(item)
        else:
            return True
    return False