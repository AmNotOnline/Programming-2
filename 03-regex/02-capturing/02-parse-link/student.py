import re

# Write your code here
def parse_link(string):
    m = re.fullmatch(r'<a.*href=\"(.*)\">(.*)</a>', string)
    if m == None: return None
    return (m[2], m[1]) 