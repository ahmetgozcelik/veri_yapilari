# def hashFunction(key):
#     myHash = 0
#     for letter in key:
#         myHash = (myHash + ord(letter) * 19)
#     return myHash
# print(hashFunction("apple"))
# print(hashFunction("appl"))



from typing import Self


def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip(" "), 1)
    )
print(hash_function("apple"))
print(hash_function("appl"))

class HashTable:

    def __init__(self, size = 13):
        self.dataMap = [None] * size

    def hashFunction(self, key):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 19) % len(self.dataMap)
        return myHash
    
    def setItem(self, key, value):
        index = self.hashFunction(key)

        if self.dataMap[index] == None:
            self.dataMap[index] = []
        self.dataMap[index].append([key, value])

    def getItem(self, key):
        index = self.hashFunction(key)
        
        if self.dataMap[index] is not None:
            for i in range(len(self.dataMap[index])):
                if self.dataMap[index][i][0] == key:
                    return self.dataMap[index][i][1]
        return None
    
    def getKeys(self):
        keys = []
        for i in range(len(self.dataMap)):
            if self.dataMap[i] is not None:
                for j in range(len(self.dataMap[i])):
                    keys.append(self.dataMap[i][j][0])
        return keys
    
    def printTable(self):
        for index,value in enumerate(self.dataMap):
            print(index, "-> ", value)


myHashTable = HashTable()
print(myHashTable.setItem('Apple', 100))
print(myHashTable.setItem('Banana', 200))
print(myHashTable.setItem('Melon', 250))
print(myHashTable.printTable())

print("--------------------------------")

print(myHashTable.setItem('a', 300))
print(myHashTable.setItem('b', 100))
print(myHashTable.setItem('c', 150))
print(myHashTable.printTable())

