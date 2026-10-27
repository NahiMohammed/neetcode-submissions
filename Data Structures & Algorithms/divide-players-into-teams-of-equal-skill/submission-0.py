class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)%2 ==1 :
            return -1

        skill.sort()
        s = 0
        l = 0 
        r = len(skill) -1
        res=0
        while l<r :
            if s == 0 :
                s+=skill[l]+skill[r]
                res+=skill[l]*skill[r]
                l+=1
                r-=1
            else :
                if skill[l]+skill[r]!=s :
                    return -1

                else :
                    res+=skill[l]*skill[r]
                    l+=1
                    r-=1
        return res
