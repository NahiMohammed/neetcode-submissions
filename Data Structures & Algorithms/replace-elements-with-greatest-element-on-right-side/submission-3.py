class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max=arr[-1]
        
        for i in range(len(arr)-2,-1,-1) :
            tmp=curr_max
            if arr[i]>curr_max :
                tmp=arr[i]
            arr[i]=curr_max
            curr_max=tmp
        arr[-1]=-1
        return arr


        