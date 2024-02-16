# Write your code here
def median(ns: list):
    if len(ns) == 1:
        return ns[0]
    
    ns.sort()
    if len(ns) % 2:
        return ns[len(ns) // 2]
    else:
        return (ns[len(ns) // 2 - 1] + ns[(len(ns) // 2)]) / 2