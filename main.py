#Initializing the Graph Class
from typing import DefaultDict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = DefaultDict(list)
        self.distances = {}
    
    def addNode(self,value):
        self.nodes.add(value)
    
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance