# Write your code here
def keys_with_value(dictionary: dict, value):
    out = []
    for key in dictionary:
        if dictionary[key] == value:
            out.append(key)
    return out