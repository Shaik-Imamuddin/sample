class Solution:
    def dfs(self, adj):
        res = []
        stack = [0]

        visited = [False] * len(adj)


        while stack:
            currnode = stack.pop()
            
            if visited[currnode]:
                continue
            
            visited[currnode]=True
            res.append(currnode)

            for i in reversed(adj[currnode]):
                if not visited[i]:
                    stack.append(i)

        return res