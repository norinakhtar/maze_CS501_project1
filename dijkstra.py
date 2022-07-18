       
from typing import DefaultDict
from main import Graph  
def dijkstra(graph, initial):
        visited = {initial : 0}
        path = DefaultDict(list)

        nodes = set(graph.nodes)

        while nodes:
            output = 0
            minNode = None
            for node in nodes:
                if node in visited:
                    if minNode is None:
                        minNode = node
                    elif visited[node] < visited[minNode]:
                        minNode = node
            if minNode is None:
                break

            nodes.remove(minNode)
            currentWeight = visited[minNode]

            for edge in graph.edges[minNode]:
                weight = currentWeight + graph.distances[(minNode, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge].append(minNode)
            # output += visited.values()
        dict = visited.values()
        total = sum(dict)
        print("Output:",total)
        return visited, path

customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addEdge("A", "B", 1)
customGraph.addEdge("A", "D", 2)
customGraph.addEdge("B", "C", 2)
customGraph.addEdge("C", "D", 2)
customGraph.addEdge("C", "E", 8)
# customGraph.addEdge("D", "C", 2)
customGraph.addEdge("D", "E", 3)

print(dijkstra(customGraph, "A"))
