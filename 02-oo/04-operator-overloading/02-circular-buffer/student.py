class CircularBuffer:
    def __init__(self, max_size) -> None:
        self.__size = max_size
        self.__contents = []
    
    def add(self, item):
        if len(self.__contents) == self.__size:
            self.__contents = self.__contents[1:]
        self.__contents.append(item)
    
    def __getitem__(self, idx):
        return self.__contents[idx]

    def __len__(self):
        return len(self.__contents)
