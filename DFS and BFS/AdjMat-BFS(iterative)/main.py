class Graph:
    def __init__(self,v):
        self.vertices = v
        self.adjMatrix = [[0 for j in range(v)] for i in range(v)]

    def addEdge(self,u,v):
        self.adjMatrix[u][v]=1
        self.adjMatrix[v][u]=1
    
    def display(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.adjMatrix[i][j],end=" ")
            print()
    
    def bfs(self,start):
        visited = [False]*self.vertices
        queue=[start]
        visited[start] = True
        
        while queue:
            currnode = queue.pop(0)
            print(currnode,end=" ")
            
            # check the unvisited neighobures
            # and mark them visited   
            for i in range(self.vertices):
                if self.adjMatrix[currnode][i]==1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
        print()
    
n=int(input())
g=Graph(n)

while True:
    u,v = map(int,input().split())
    if u==-1 and v ==-1:
        break
    g.addEdge(u,v)

g.display()
start = int(input())
g.bfs(start)