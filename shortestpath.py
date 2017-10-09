import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
        self.time = []
        self.sumtime_node = []
        self.mintime_node = []
        self.short_path = []              
 
    def printSolution(self, dist):
        print ("Vertex tDistance from Source")
        print(dist)
        for node in range(self.V):
            print (node,"t",dist[node])
 
    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initilaize minimum distance for next node
        min = sys.maxsize
 
        # Search not nearest vertex not in the 
        # shortest path tree
        for v in range(self.V):
            if (dist[v] < min and sptSet[v] == False):
                min = dist[v]
                min_index = v
 
        return min_index
 
    # Funtion that implements Dijkstra's single source 
    # shortest path algorithm for a graph represented 
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration

            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the 
            # shotest path tree
            sptSet[u] = True
 
            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if(self.graph[u][v] > 0 and sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                        dist[v] = dist[u] + self.graph[u][v]
                        # print(self.graph[u][v], " ", dist[u], " ", dist[v])
                        self.time.append(self.graph[u][v])
                        self.sumtime_node.append(dist[u])
                        self.mintime_node.append(dist[v])

                        
 
        # self.printSolution(dist)
        mintime = dist[10]   # 4 -> destination node
        while(True):
        	index = self.mintime_node.index(mintime)
        	self.short_path.append(self.time[index])
        	mintime = self.sumtime_node[index]
        	if(sum(self.short_path) == dist[10]):
        		break
        print("shortest path with time :", list(reversed(self.short_path)))		
 
# Driver program
# g  = Graph(9)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#            [4, 0, 8, 0, 0, 0, 0, 11, 0],
#            [0, 8, 0, 7, 0, 4, 0, 0, 2],
#            [0, 0, 7, 0, 9, 14, 0, 0, 0],
#            [0, 0, 0, 9, 0, 10, 0, 0, 0],
#            [0, 0, 4, 14, 10, 0, 2, 0, 0],
#            [0, 0, 0, 0, 0, 2, 0, 1, 6],
#            [8, 11, 0, 0, 0, 0, 1, 0, 7],
#            [0, 0, 2, 0, 0, 0, 6, 7, 0]
#           ];
# g.dijkstra(0);
# g = Graph(5)
# g.graph = [[0, 10, 0, 1, 0],
# 		   [0, 0, 5, 15, 0],
# 		   [5, 0, 0, 2, 4],
# 		   [1, 15, 2, 0, 0],
# 		   [0, 0, 4, 0, 0]
# 		  ];
# g.dijkstra(0);

g = Graph(15)
#           0 1 2 3 4 5 6 7 8 9 1011121314  
g.graph = [[0,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
		   [0,0,10,0,0,0,0,0,0,0,0,0,1,0,0],
		   [10,0,0,12,0,0,0,0,0,0,0,0,0,0,0],
		   [0,0,12,0,11,0,0,2,0,0,0,0,0,0,0],
		   [0,0,0,11,0,15,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,15,0,4,0,0,0,0,0,0,0,9],
		   [0,0,0,0,0,4,0,5,0,0,0,0,0,1,0],
		   [0,0,0,2,0,0,5,0,0,0,0,4,0,0,0],
		   [0,0,0,0,0,0,0,0,0,5,10,0,0,0,0],
		   [0,0,0,0,0,0,0,0,5,0,0,0,0,0,3],
		   [0,0,0,0,0,0,0,0,10,0,0,0,0,1,0],
		   [0,0,0,0,0,0,0,4,0,0,0,0,3,0,0],
		   [0,1,0,0,0,0,0,0,0,0,0,3,0,0,0],
		   [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0],
		   [0,0,0,0,0,9,0,0,0,3,0,0,0,0,0],
		  ];

g.dijkstra(0);		  
