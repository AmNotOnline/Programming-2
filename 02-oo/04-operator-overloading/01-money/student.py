class Money:
    def __init__(self, amount, currency) -> None:
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        
        raise RuntimeError("Mismatched currencies!")
    
    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        
        raise RuntimeError("Mismatched currencies!")
    
    def __mul__(self, val):
        return Money(self.amount * val, self.currency)
