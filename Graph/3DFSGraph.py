def dfs(adj):
    ans=[]
    visited=[0] * (n) 
    def solve( node ,ans, visited,adj): 
        visited[node] =1 
        ans.append(node) 

        for i in adj[node] :
            if visited[i] ==0:
                solve( i ,ans, visited,adj)
    
    solve( 0 ,ans, visited,adj) 
    return ans