from Match import Match
from collections import deque

class Solution:
    
    def __init__(self, m, n, hospital_list, student_list, hosp_open_slots):
        """
            The constructor exists only to initialize variables. You do not need to change it.
            :param m: The number of hospitals
            :param n: The number of students
            :param hospital_list: The preference list of hospitals, as a dictionary.
            :param student_list: The preference list of the students, as a dictionary.
            :param hosp_open_slots: Open slots of each hospital
            """
        self.m = m
        self.n = n
        self.hospital_list = hospital_list
        self.student_list = student_list
        self.hosp_open_slots = hosp_open_slots
    
    def get_matches(self):
        
        free = deque(self.student_list.keys())
        hs = list(self.hospital_list.keys())
        matches = {hospital : [] for hospital in hs}
        studentprop = {stuff : 0 for stuff in free}

        ranks = {}
        for hospital in self.hospital_list:
            ranks[hospital] = {}
            for rank, student in enumerate(self.hospital_list[hospital]):
                ranks[hospital][student] = rank

        while free:
            cur = free.popleft()
            propl = self.student_list.get(cur)

            if studentprop[cur] < len(propl):
                curh = propl[studentprop[cur]] 
                studentprop[cur] += 1

            else:
                continue
            
            if self.hosp_open_slots[curh] > 0:
                matches[curh].append(cur)
                self.hosp_open_slots[curh] -= 1
            else:
                worst = -1
                sworst = None
                for its in matches[curh]:
                    thr = ranks[curh][its]
                    if thr > worst:
                        worst = thr
                        sworst = its
                if ranks[curh][cur] < worst:
                    matches[curh].remove(sworst)
                    matches[curh].append(cur)
                    free.append(sworst)
                else:
                    free.append(cur)

        return[Match(hospital, student) for hospital, students in matches.items() for student in students]
    

        


                        
                
            

            

        

                    

        


        
