class Board:
    def __init__(self, width, height, colP1: int, colP2: int) -> None:
        self.__width = width
        self.__height = height
        self.colP1 = colP1
        self.colP2 = colP2
        self.__board = [[] for i in range(width)]
        for row in self.__board:
            row.extend([0 for _ in range(width)])
    
    def print(self):    
        def set_fg_col(col):
            return f"\033[{col}m"
        
        out = "\033[2J"
        out += f"+{(4 * self.__width - 1) * '-'}+\n"
        for row in self.__board:
            for mark in row:
                if mark == 0:
                    out += "|   "
                elif mark == 1:
                    out += f"{set_fg_col(97)}|{set_fg_col(self.colP1)} O "
                else:
                    out += f"{set_fg_col(97)}|{set_fg_col(self.colP2)} O "
            out += f"{set_fg_col(97)}|\n"
            out += f"+{(4 * self.__width - 1) * '-'}+\n"
        print(out)
    
    def add(self, column: int):
        if column > self.__width:
            raise ValueError