from typing import List

class Iterator:
    def __init__(self, collection: List[int]):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index >= len(self._collection):
            raise StopIteration()

        value = self._collection[self._index]
        self._index += 1
        return value

class Collection:
    def __init__(self):
        self._data = []

    def add_item(self, item: int):
        self._data.append(item)

    def __iter__(self):
        return Iterator(self._data)

if __name__ == "__main__":
    collection = Collection()
    collection.add_item(1)
    collection.add_item(2)
    collection.add_item(3)

    for item in collection:
        print(item)