# Write your code here
def target_sum(ns: list[int], target: int):
    for x in range(len(ns)):
        for y in range(x, len(ns)):
            if ns[x] + ns[y] == target:
                return True
    return False