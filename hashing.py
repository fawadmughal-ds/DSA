
# Example concrete implementation of AbstractHashTable:
class SimpleHashTable():
    def __init__(self, size=101):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        # Check if the key already exists and update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    
    def search(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]
                    return
    
    def __getitem__(self, key):
        return self.search(key)
    
    def __setitem__(self, key, value):
        self.insert(key, value)
    
    def __delitem__(self, key):
        self.delete(key)

# Example usage
hash_table = SimpleHashTable()
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)

print("Search for 'apple':", hash_table.search("apple"))
print("Search for 'banana':", hash_table.search("banana"))

hash_table["cherry"] = 30
print("Search for 'cherry':", hash_table["cherry"])

del hash_table["banana"]
print("Search for 'banana' after deletion:", hash_table.search("banana"))
