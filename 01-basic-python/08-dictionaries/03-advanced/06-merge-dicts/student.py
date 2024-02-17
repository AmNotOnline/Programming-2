# Write your code here
def merge_dicts(dict1: dict, dict2: dict):
    out = {}
    for key in dict1: out[key] = dict1[key]
    for key in dict2: out[key] = dict2[key]
    return out