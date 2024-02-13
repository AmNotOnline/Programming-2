# Write your code here
def card_value(string):
    match string:
        case "Jack":
            return 11
        
        case "Queen":
            return 12
        
        case "King":
            return 13
        
        case "Ace":
            return 1
        
        case _:
            return int(string)
