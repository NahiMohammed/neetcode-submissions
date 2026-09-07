import bisect
class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)
        self.map_time= defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append(value)
        self.map_time[key].append(timestamp)
    
    

    def get(self, key: str, timestamp: int) -> str:
        if len(self.map_time[key])==1 :
            return self.map[key][0]
        print(f"get : {self.map} ;;;, {self.map_time}")
        idx=bisect.bisect_right(self.map_time[key],timestamp) 
        
        return self.map[key][idx-1] 

        
