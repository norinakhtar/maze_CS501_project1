# def prims(self):
#             INF = 9999999
#             # number of vertices in graph
#             N = 5
#             #creating graph by adjacency matrix method
#             G = [[0, 19, 5, 0, 0],
#                 [19, 0, 5, 9, 2],
#                 [5, 5, 0, 1, 6],
#                 [0, 9, 1, 0, 1],
#                 [0, 2, 6, 1, 0]]

#             selected_node = [0, 0, 0, 0, 0]

#             no_edge = 0

#             selected_node[0] = True

#             # printing for edge and weight
#             print("Edge : Weight\n")
#             while (no_edge < N - 1):
                
#                 minimum = INF
#                 a = 0
#                 b = 0
#                 for m in range(N):
#                     if selected_node[m]:
#                         for n in range(N):
#                             if ((not selected_node[n]) and G[m][n]):  
#                                 # not in selected and there is an edge
#                                 if minimum > G[m][n]:
#                                     minimum = G[m][n]
#                                     a = m
#                                     b = n
#                 print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
#                 selected_node[b] = True
#                 no_edge += 1




#####################################################################



#Function to implement Prim's Algorithm
    # def primsAlgo(self):
    #     visited = [0]*self.vertexNum
    #     edgeNum=0
    #     visited[0]=True
    #     while edgeNum<self.vertexNum-1:
    #         min = sys.maxsize
    #         for i in range(self.vertexNum):
    #             if visited[i]:
    #                 for j in range(self.vertexNum):
    #                     if ((not visited[j]) and self.edges[i][j]):
    #                         if min > self.edges[i][j]:
    #                             min = self.edges[i][j]
    #                             s = i
    #                             d = j
    #         self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
    #         visited[d] = True
    #         edgeNum += 1
    #     self.printSolution()







# edges = [[0, 10, 20, 0, 0],
#             [10, 0, 30, 5, 0],
#             [20, 30, 0, 15, 6],
#             [0, 5, 15, 0, 8],
#             [0, 0, 6, 8, 0]]

# nodes = ["A","B","C","D","E"]
# g = Graph(5, edges, nodes)






####################################################
# from typing import List


# class Solution:
#     def minimumCost(self, N: int, connections: List[List[int]]) -> int:
#         def find(i):
#             while parent[i] != i:
#                 i = parent[i]
#             return i
        
#         def union(i, j):
#             if rank[i] == rank[j]:
#                 parent[i] = j
#                 rank[j] += 1
#             elif rank[i] > rank[j]:
#                 parent[j] = i
#             else:
#                 parent[i] = j
        
#         connections.sort(key=lambda x: x[2])
#         count = 0
#         res = 0
#         rank = [0] * (N+1)
#         parent = [i for i in range(N+1)]
        
#         for x, y, d in connections:
#             x = find(x)
#             y = find(y)
#             if x != y:
#                 union(x, y)
#                 count += 1
#                 res += d

#         if count == N-1:
#             return res
#         return -1


# if __name__ =="__main__":
#     n = 3 
#     connections =[[1,2,5],[1,3,6],[2,3,1]]
#     s= Solution()
#     print(s.minimumCost(n,connections))



#Initializing the Graph Class