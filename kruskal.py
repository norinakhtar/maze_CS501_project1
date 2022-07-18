
from kmsp import DisjointSet
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self,s,d,w):
        cost = 0

        for s, d, w in self.MST:
            cost += w
            print("%s - %s: %s" % (s, d, w))
        print("Minimum Spanning Tree: " , cost)


          #Function to implement Kruskal's Algorithm
    def kruskalAlgo(self):
        i, e = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s,d,w])
                ds.union(x,y)
        self.printSolution(s,d,w)


    
##test       
g = Graph(7)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addNode("F")
g.addNode("G")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 3)
g.addEdge("B", "C", 4)
g.addEdge("B", "D", 6)
g.addEdge("B", "E", 2)
g.addEdge("C", "D", 5)
g.addEdge("C", "F", 6)
g.addEdge("D", "E", 6)
g.addEdge("D", "F", 6)
g.addEdge("E", "G", 5)
g.addEdge("E", "F", 3)
g.addEdge("F", "G", 4)
g.kruskalAlgo()












    