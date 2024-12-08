from collections import deque, defaultdict, OrderedDict
class Solution:

    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph

    def output_distances(self):
        #maximus = max(max(value) for value in self.graph.values())
        visited = {}
        arr = {}
        arr = defaultdict(lambda: -1,arr)
        
        #visited = [False] * (maximus + 1)
        #arr = [-1] * (maximus + 1)
        queue = deque([self.start_node])
        #arr[self.start_node] = 0
        visited[self.start_node] = True
        arr[self.start_node] = 0
    
        

        while queue:
            curnode = queue.popleft()

            for nxnode in self.graph.get(curnode,[]):      
                    if nxnode not in visited:
                        arr[nxnode] = arr[curnode] + 1
                        queue.append(nxnode)
                        visited[nxnode] = True
                        
        d2 = OrderedDict(arr)

        return d2
