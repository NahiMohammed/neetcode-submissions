class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last=arr[-1]
        arr[-1]=-1
        for i in range(len(arr)-2,-1,-1):
            tmp=last
            if arr[i]>last :
                last=arr[i]
            arr[i]=tmp
        return arr

        