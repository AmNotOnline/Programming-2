# Write your code here
import re
def is_number(string):
    return re.fullmatch(r'\d+(\.\d+)?', string)
