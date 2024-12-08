import math
class Solution:
    def __init__(self, points):
        self.points = points

    def findClosestPair(self):
        n = len(self.points)
        if n <= 3:
            return self.fcpHelper(self.points)
        else:
            x = sorted(self.points, key=lambda x: x[0])
            mid = n // 2
            xs = x[mid][0]
            left_points = x[:mid]
            right_points = x[mid:]
            left = Solution(left_points)
            right = Solution(right_points)
            ld = left.findClosestPair()
            rd = right.findClosestPair()
            d = min(ld, rd)
            strip = [p for p in x if abs(p[0] - xs) < d]
            strip.sort(key=lambda x: x[1])
            min_strip = d
            for i in range(len(strip)):
                j = i + 1
                while j < len(strip) and (strip[j][1] - strip[i][1]) < min_strip:
                    dist = self.distance(strip[i], strip[j])
                    if dist < min_strip:
                        min_strip = dist
                    j += 1
            return min(d, min_strip)
        
    

    def fcpHelper(self,p):
        sm = float('inf')
        n = len(p)
        for i in range(n):
            for j in range(i+1, n):
                d = self.distance(p[i], p[j])
                if d < sm:
                 sm = d
        return sm

    def distance(self,p1,p2):
        return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

        
        
