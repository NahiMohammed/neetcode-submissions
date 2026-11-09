class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res= 0 
        s = 0 
        for r in range(k) :
            s+=arr[r]
        if s//k>=threshold :
            res += 1
        for r in range(k,len(arr)) :
            s+=arr[r]
            s-=arr[r-k]
            if s//k>=threshold :
                res += 1
        return res
        