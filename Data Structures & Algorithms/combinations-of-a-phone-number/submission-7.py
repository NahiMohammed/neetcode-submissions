class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits :
            return []
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res=[]
        subset=[]
        def back(idx):
            print(subset)
            if len(subset)==len(digits) :
                res.append("".join(subset))
                return 
            for i in range(idx , len(digits)) :
                for c in dic[digits[i]] :
                    subset.append(c)
                    back(i+1)
                    subset.pop()
        back(0)


        return res
        