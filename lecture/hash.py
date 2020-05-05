'''
[ "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]
#    0      1          2        3       4         5              6           7     

"beej"
"elit"

iteration = O(n)


f("elit") -> 7
f("ipsum") -> 1
f("foobar") -> 1 

# ord() 
# .encode - returns the byte value
# man ascii

bytes = "beej".encode()
for i in bytes:
    print(i)

1. Get bytes for the key
2. Make up a function that returns an index for those bytes
    * Adding the bytes
    * Modding with the hash table size
'''

# dependent on the size of the key but not the hash table size
# order 1

hash_table_size = 8

hash_table = [None] * hash_table_size

def myhash(s):
    str_bytes = s.encode()

    total = 0

    for b in str_bytes:
        total += b
    
    return total

def hash_index(s):
    h = myhash(s)

    return h % hash_table_size

def put(key, value):
    # Get the index into the hash table list
    index = hash_index(key)
    hash_table[index] = value

def get(key):
    index = hash_index(key)
    return hash_table[index]

def delete(key):
    index = hash_index(key)
    hash_table[index] = None

if __name__ == "__main__":
    # If running from the command line 
    # print(hash_index("Hello")) # 4
    # print(hash_index("foobar")) # 1
    # print(hash_index("cats")) # 3
    # print(hash_index("beej")) # 6
    # print(hash_index("foobaz")) # 1
    # print(hash_index("qux")) # 6

    # print(hash_table)
    put("Hello", 37) # similar to dict: d["Hello"] = 37
    put("foobar", 128)
    put("cats", "dogs")
    # print(hash_table)

    print(get("Hello"))
    # print(get("beej"))

    delete("Hello")
    print(get("Hello")) # None