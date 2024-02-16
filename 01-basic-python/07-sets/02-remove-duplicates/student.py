# Write your code here
def remove_duplicates(xs: list):
    unq = set()
    out = []
    for i in xs:
        if i not in unq:
            out.append(i)
            unq.add(i)
    
    return out