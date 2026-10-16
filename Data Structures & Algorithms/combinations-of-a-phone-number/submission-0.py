class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0 :
            return []
        phone = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        res=[]
        sub=[]
        def backtracking(start) :
            if len(sub)==len(digits) :
                res.append("".join(sub))
                return 
            for i in range(start,len(digits)) :
                for c in phone[digits[i]] :
                    sub.append(c)
                    backtracking(i+1)
                    sub.pop()
                    


        backtracking(0)
        return res
        