import re

def parse_time(string):
    m = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})([.:](\d{3}))?', string)
    if m == None:
        return None
    else:
        return (int(m[1]), int(m[2]), int(m[3]), int(m[5] or 0))