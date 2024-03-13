# Write your code here
import re
def is_valid_password(string: str):
    return len(string) >= 12 \
        and re.search(r'\d', string) \
        and re.search(r'[a-z]', string) \
        and re.search(r'[A-Z]', string) \
        and re.search(r'[+\-*/.@]', string) \
        and not re.search(r'(.)\1\1', string) \
        and not re.search(r'(.)*.\1*.\1*.\1', string)
            
