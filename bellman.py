#Initializing the Graph Class
class Graph:
    def __init__(self, vertices):
        self.V = vertices   
        self.graph = []     
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def addNode(self,value):
        self.nodes.append(value)

    def print_solution(self, dist):
        cost = 0
        print("Distance of Vertex from Source")
        for key, value in dist.items():
            cost += value
            print('  ' + key, ' :    ', value)
        print("Output: ",cost)
    


    #Implementing Bellman-Ford's Algorithm
    def bellmanFord(self, src):
        dist = {i : float("Inf") for i in self.nodes}
        dist[src] = 0
        for temp in range(self.V-1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
            
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative cycle")
                return
            

        self.print_solution(dist)



g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "B", 1)
g.add_edge("A", "D", 2)
g.add_edge("B", "C", 2)
g.add_edge("C", "D", 2)
g.add_edge("C", "E", 8)
g.add_edge("D", "C", 2)
g.add_edge("D", "E", 3)
g.bellmanFord("A")
