# Write your code here
def target_sum(ns: list[int], target: int):
    for x in range(len(ns)):
        if x == len(ns) - 1:
            return False
        
        for y in range(x + 1, len(ns)):
            if ns[x] + ns[y] == target:
                return True