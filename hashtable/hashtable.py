class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        """
        hash = 134206661369
        
        for x in key:
            hash = hash * 69666420
            hash = hash * ord(x)
        
        return hash


    def djb2(self, key):
        """
        DJB2 32-bit hash function
        """
        hash = 5381

        for x in key:
            hash = hash * 33 + ord(x)
        
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        """
        index = self.hash_index(key)
        self.storage[index] = HashTableEntry(key, value)
            



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        """
        index = self.hash_index(key)
        self.storage[index] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        """
        index = self.hash_index(key)

        if self.storage[index] == None:
            return None
        else:
            return self.storage[index].value


    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        """
        wizened = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for entry in wizened:
            if entry == None: 
                continue
            else:
                self.put(entry.key, entry.value)



if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
