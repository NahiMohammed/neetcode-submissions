from _bisect import bisect_left
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data :
            self.data[key]= [[],[]]
        self.data[key][0].append(timestamp)
        self.data[key][1].append(value)


        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        i = bisect_right(self.data[key][0],timestamp)
        if i == 0 :
            return ""

        return self.data[key][1][i-1]
        
