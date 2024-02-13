# Write your code here
def coins(one, two, five, goal):
    for f in range(five + 1):
        for t in range(two + 1):
            for o in range(one + 1):
                if 5*f + t*2 + o == goal:
                    return True
    return False