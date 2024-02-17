class AssocList:
    def __init__(self) -> None:
        self.__items: list[list] = []

    
    def __setitem__(self, key, value):
        for i in range(len(self.__items)):
            if self.__items[i][0] == key:
                self.__items[i][1] = value
                return
        self.__items.append([key, value])

    
    def __getitem__(self, key):
        for i in range(len(self.__items)):
            if self.__items[i][0] == key:
                return self.__items[i][1]
        raise KeyError()

    
    def __len__(self):
        return len(self.__items)
    

    def keys(self) -> list:
        return [self.__items[i][0] for i in range(len(self.__items))]
    

    def values(self) -> list:
        return [self.__items[i][1] for i in range(len(self.__items))]