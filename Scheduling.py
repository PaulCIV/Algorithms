from collections import deque
class Solution:
    
    def __init__(self, listOfRallies):
        self.rallies = listOfRallies
    
    def getSchedule(self):
        time = 0
        fin = deque()
        d = {}
        for stuff in range(len(self.rallies)):
            d[self.rallies[stuff]] = stuff
        
        self.rallies.sort(key = lambda x: (x[1],x[0]))
        
        for things in self.rallies:
            if time  + things[0] > things[1]:
                return []  
            else:
            
                fin.append((d[things],time))
                time += (things[0])
                
            

        
        return fin
