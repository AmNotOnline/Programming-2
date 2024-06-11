# Enter your code here:

from abc import ABC, abstractmethod
import re

class StorageDevice:
    def __init__(self, block_count: int, block_size: int) -> None:
        self.__available_blocks = set(range(block_count))
        self.__used_blocks = set()
        self.__block_size = block_size

    
    def allocate(self, block_count: int) -> list[int]:
        if self.available_block_count < block_count:
            raise RuntimeError('Insufficient unused blocks.')

        allocated = [self.__available_blocks.pop() for _ in range(block_count)]
        self.__extend_set(self.__used_blocks, allocated)
        return allocated

    def free(self, blocks: list[int]):
        if any(block not in self.__used_blocks for block in blocks):
            raise RuntimeError('Free block submitted for freeing.')

        self.__extract_set(self.__used_blocks, blocks)
        self.__extend_set(self.__available_blocks, blocks)        
    

    def __extend_set(self, collection: set, iterable):
        [collection.add(i) for i in iterable]
    
    def __extract_set(self, collection: set, iterable):
        [collection.remove(i) for i in iterable]

    
    @property
    def available_block_count(self) -> int:
        return len(self.__available_blocks)
    
    @property
    def used_block_count(self) -> int:
        return len(self.__used_blocks)
    
    @property
    def total_block_count(self) -> int:
        return self.available_block_count + self.used_block_count
    
    @property
    def block_size(self) -> int:
        return self.__block_size


class Entity(ABC):
    def __init__(self, storage: StorageDevice, name: str) -> None:
        super().__init__()

        self.__storage_device = storage
        self.__name = name
    
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if not self.is_valid_name(new_name):
            raise RuntimeError('Invalid name.')

        self.__name = new_name
    

    @property
    def storage(self) -> StorageDevice:
        return self.__storage_device

    
    @property
    @abstractmethod
    def size_in_blocks(self) -> int:
        pass

    @property
    def size_in_bytes(self) -> int:
        return self.size_in_blocks * self.storage.block_size


    @abstractmethod
    def clear(self):
        pass


    @staticmethod
    def is_valid_name(name):
        return re.search(r"[^0-9A-Za-z.]", name) == None


class File(Entity):
    def __init__(self, storage: StorageDevice, name: str) -> None:
        super().__init__(storage, name)
        
        self.__used_blocks = set()
    

    def grow(self, block_count: int):
        self.__extend_set(
            self.__used_blocks, 
            self.storage.allocate(block_count)
        )

    @property
    def size_in_blocks(self) -> int:
        return len(self.__used_blocks)
    
    def clear(self):
        self.storage.free(list(self.__used_blocks))
        self.__used_blocks = set()


    def __extend_set(self, collection: set, iterable):
        [collection.add(i) for i in iterable]


class Directory(Entity):
    def __init__(self, storage: StorageDevice, name: str) -> None:
        super().__init__(storage, name)

        self.__children = set()
    
    def add(self, entity: Entity):
        self.__children.add(entity)
    
    @property
    def size_in_blocks(self) -> int:
        return sum(child.size_in_blocks for child in self.__children)
    
    def clear(self):
        [child.clear() for child in self.__children]
        self.__children = set()


def test_storage_device_init():
    storage = StorageDevice(10, 5)

    assert storage.available_block_count == 10
    assert storage.used_block_count == 0
    assert storage.block_size == 5

def test_storage_device_allocate_free():
    storage = StorageDevice(10, 5)

    assert len(storage.allocate(5)) == 5
    assert storage.used_block_count == 5
    assert storage.used_block_count == 5
    assert storage.block_size == 5


def test_file_grow():
    storage = StorageDevice(10, 5)
    file = File(storage, "test_file")

    file.grow(3)
    assert file.size_in_blocks == 3
    assert storage.used_block_count == 3

    file.grow(2)
    assert file.size_in_blocks == 5
    assert storage.used_block_count == 5

def test_file_clear():
    storage = StorageDevice(10, 5)
    file = File(storage, "test_file")

    file.grow(3)
    file.clear()
    assert file.size_in_blocks == 0
    assert storage.used_block_count == 0

def test_directory_add():
    storage = StorageDevice(10, 5)
    directory = Directory(storage, "test_directory")
    file = File(storage, "test_file")

    directory.add(file)
    assert directory.size_in_blocks == file.size_in_blocks
    assert storage.used_block_count == file.size_in_blocks

def test_directory_clear():
    storage = StorageDevice(10, 5)
    directory = Directory(storage, "test_directory")
    file = File(storage, "test_file")

    directory.add(file)
    directory.clear()
    assert directory.size_in_blocks == 0
    assert storage.used_block_count == 0