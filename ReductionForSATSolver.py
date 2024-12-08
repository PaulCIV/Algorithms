class Solution:

    def __init__(self, graph, k):
        self.k = k
        self.graph = graph

    def output_clauses(self):
        kk = 1
        twod = [[0] * self.k for _ in range(len(self.graph))]
    
        for n in range(0, len(self.graph.keys())): 
            for c in range(1, self.k + 1):  
                twod[n][c - 1] = kk  
                kk += 1

        clauses = []

        for n in self.graph.keys():
            p = [(n, c) for c in range(1, self.k + 1)]
            clauses.append((p, [])) 

        for n in self.graph.keys():
            for c1 in range(1, self.k + 1):
                for c2 in range(c1 + 1, self.k + 1):  
                    clauses.append(([], [(n, c1), (n, c2)]))

        
        beento = set()  
        for u in self.graph.keys():
            for v in self.graph[u]:
                if (u, v) not in beento and (v, u) not in beento:
                    for c in range(1, self.k + 1):
                        clauses.append(([], [(u, c), (v, c)]))  
                    beento.add((u, v))  
        

        
        return clauses
