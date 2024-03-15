import re

# Write your code here
def collect_links(string):
    return re.findall(r'<a.*href=\"(.*)\">.*</a>', string)
