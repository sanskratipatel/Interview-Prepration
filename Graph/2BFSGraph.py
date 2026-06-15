class Solution:
    def bfs(self, adj):
        # code here 
        n = len(adj) 
       
      
        queue = deque([0]) 
        ans = [] 
        visited = [0] * (n)  
        
        visited[0] = 1 
        
        while len(queue) != 0 : 
            e = queue.popleft() 
            ans.append(e) 
            for node in adj[e] : 
                if visited[node] == 0 : 
                    queue.append(node) 
                    visited[node] =1 
        return ans
        
        