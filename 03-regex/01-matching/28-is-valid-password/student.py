# Write your code here
import re
def is_valid_password(string: str):
    return re.fullmatch(
            r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[+\-*/.@])(?!.*(.)\1\1)(?!.*(.)(.*\2){3,}).{12,}',
            string
        ) 
