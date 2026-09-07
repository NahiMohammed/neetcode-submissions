import bisect
class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)
        self.map_time= defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append(value)
        self.map_time[key].append(timestamp)
    
    

    def get(self, key: str, timestamp: int) -> str:

        idx=bisect.bisect_right(self.map_time[key],timestamp) 
        if idx==0 :
            return ""
        
        return self.map[key][idx-1] 

        
