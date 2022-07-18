INF = 9999999
# number of vertices in graph
N = 7
cost =0

#creating graph by adjacency matrix method
G = [[0, 5, 3, 0, 0,0,0],
     [5, 0, 4, 6, 2,0,0],
     [3, 4, 0, 5, 0,6,0],
     [0, 6, 5, 0, 6,6,0],
     [0, 2, 0, 6, 0,3,5],
     [0, 0, 6, 6, 3,0,4],
     [0, 0, 0, 0, 5,4,0]]

selected_node = [0, 0, 0, 0, 0,0,0]

no_edge = 0

selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")

while (no_edge < N - 1):
    minimum = INF
    a = 0
    b = 0
    for m in range(N):

        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
                        cost += m
        print("======cost",cost)
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    print(",,,,,", G[a][b])
    selected_node[b] = True
    print( selected_node[b])
    no_edge += 1
print("cost....",cost)



    # a=0,b=1,c=2,d=3,e=4,f=5,g=6
    
# 0-2:3    a - c =3
# 2-1:4    c-b = 4
# 1-4:2    b-e = 2
# 4-5:3    e-f =3
# 5-6:4    f-g = 4
# 2-3:5    c-d =5
    