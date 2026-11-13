class Solution:
    def bfs(self, adj):
        # code here
        res = []
        queue = []
        
        visited = [False]*len(adj)
        
        queue.append(0)
        visited[0] = True
        
        while queue:
            currnode = queue.pop(0)
            res.append(currnode)
            
            for i in adj[currnode]:
                if not visited[i]:
                    visited[i]=True
                    queue.append(i)
            
        return res