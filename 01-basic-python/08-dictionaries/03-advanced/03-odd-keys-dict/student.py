# Write your code here
def odd_keys_dict(full: dict[int, any]):
    out = {}
    for key in full:
        if key % 2 == 1:
            out[key] = full[key]
    return out