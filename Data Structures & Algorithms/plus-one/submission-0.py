class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits==[9] :
            return [1,0]
        if digits[-1]<9 :
            digits[-1]+=1
            return digits
        else: 
            res= self.plusOne(digits[0:len(digits)-1])
            res.append(0)
            return res
        