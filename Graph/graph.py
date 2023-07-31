class Graph:
    def __init__(self):
        self.adjDict = {}

    def addVertex(self, vertex):
        if vertex not in self.adjDict.keys():
            self.adjDict[vertex] = []
            return True
        return False
    
    def addEdge(self, v1, v2):
        if v1 in self.adjDict.keys() and v2 in self.adjDict.keys():
            self.adjDict[v1].append(v2)
            self.adjDict[v2].append(v1)
            return True
        return False
    
    def removeEdge(self, v1, v2):
        if v1 in self.adjDict.keys() and v2 in self.adjDict.keys():
            try:
                self.adjDict[v1].remove(v2)
                self.adjDict[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def removeVertex(self, vertex):
        if vertex in self.adjDict.keys():
            for relatedVertex in self.adjDict[vertex]:
                self.adjDict[relatedVertex].remove(vertex)
            del self.adjDict[vertex]
            return True
        return False
    
    def printGraph(self):
        for vertex in self.adjDict:
            print(vertex, "->", self.adjDict[vertex])


myGraph = Graph()
myGraph.addVertex("IST")
myGraph.addVertex("AMS")
myGraph.addVertex("CDG")
myGraph.addVertex("JFK")

myGraph.addEdge("IST", "AMS")
myGraph.addEdge("IST", "CDG")
myGraph.addEdge("IST", "JFK")
myGraph.addEdge("AMS", "CDG")
myGraph.addEdge("AMS", "JFK")
myGraph.addEdge("CDG", "JFK")

myGraph.printGraph()
myGraph.removeVertex("JFK")
myGraph.printGraph()