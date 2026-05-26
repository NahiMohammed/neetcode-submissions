class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res=[]
        if digits=="":
            return []
        def b(idx,j,sub):
            if idx==len(digits):
                if len(sub)==len(digits):

                    res.append(sub)
                return 
            for i in range(len(dic[digits[idx]])):
                b(idx+1,0,sub+dic[digits[idx]][i])


        """
            for i in range(idx,len(digits)) :
                b(i+1,0,sub+dic[digits[i]][j])
                if j==len(dic[digits[i]]):
                    b(i+1,0,sub+dic[digits[i]][j])

                if j+1<len(dic[digits[i]]):
                    b(i,j+1,sub)
        """
        b(0,0,"")
        return res
        