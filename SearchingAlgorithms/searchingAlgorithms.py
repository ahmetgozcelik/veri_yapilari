class SearchingAlgorithms:

    def sequantialSearchUnordered(self, unorderedList, number):
        
        ix = 0
        found = False #bulundu mu

        while ix < len(unorderedList) and not found:
            if unorderedList[ix] == number:
                found = True
            else:
                ix += 1
        return found

    def sequantialSearchOrdered(self, orderedList, number):
        
        ix = 0
        found = False #bulundu mu
        tooBig = False

        while ix < len(orderedList) and not found and not tooBig:
            if orderedList[ix] == number:
                found = True
            else:
                if orderedList[ix] > number:
                    tooBig = True
                else:
                    ix += 1
        return found

    def binarySearch(self, orderedList, number):
        firstPointer = 0
        lastPointer = len(orderedList) - 1

        found = False

        while firstPointer <= lastPointer and not found:

            midPoint = (firstPointer + lastPointer) // 2 # //2 -> 2.5 yerine 2 döndürür

            if orderedList[midPoint] == number:
                found = True
            else:
                if number < orderedList[midPoint]:
                    lastPointer = midPoint - 1
                else:
                    firstPointer = midPoint + 1
        return found



search = SearchingAlgorithms()
myList = [40,20,10,4,5,19,80,2,0,14]

print(search.sequantialSearchUnordered(myList, 10))

myList.sort()
print(search.sequantialSearchOrdered(myList, 6))

print(search.binarySearch(myList, 15))