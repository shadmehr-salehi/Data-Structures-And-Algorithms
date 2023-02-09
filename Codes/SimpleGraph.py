#Simple Graph Implementation with DFS and BFS 

# ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----
class Graph:
    def __init__(self ,nodes , edges):
        self.adj =[[] for i in range(nodes)]
        self.visit = [False for i in range(nodes)]
        self.nodes = nodes
        self.edges = edges
        
    def input(self):
        for i in range(self.edges):
            v,u = map(int , input().split())
            self.adj[v].append(u)
            self.adj[u].append(v)
            
    def dfs(self ,v):
        self.visit[v] = True
        for u in self.adj[v]:
            if self.visit[u] is False:
                print(f'{v} -> {u}')
                self.dfs(u)
    
                                     
    def bfs(self, v):
        self.visit = [False for i in range(self.nodes)]
        queue = list()
        queue.append(v)
        self.visit[v] = True
        while len(queue) != 0:
            u = queue.pop(0)
            for vertex in self.adj[u]:
                if self.visit[vertex] != True:
                    queue.append(vertex)
                    self.visit[vertex] = True
                    print (f'{u} -> {vertex}')
                

def main():
    g = Graph(4, 5)
    g.input()
    g.bfs(1)
    
if __name__ == "__main__": 
    main()                
        
