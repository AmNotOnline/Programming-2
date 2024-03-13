# Write your code here
import re
def contains_no_a(string):
    return not re.search('a', string)
