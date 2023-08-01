def hashFunction(key):
    myHash = 0
    for letter in key:
        myHash = (myHash + ord(letter) * 19)
    return myHash
print(hashFunction("apple"))
print(hashFunction("appl"))



def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip(" "), 1)
    )
print(hash_function("apple"))
print(hash_function("appl"))