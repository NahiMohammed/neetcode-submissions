class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        dic = defaultdict(list)
        dic1 = defaultdict(int)
        for i in range(len(wall)) : 
            if len(wall[i])>1 :
                dic[i].append(wall[i][0])
                dic1[wall[i][0]]+=1
                for j in range(1,len(wall[i])-1) :

                    dic[i].append(dic[i][-1]+wall[i][j])

                    dic1[dic[i][-1]]+=1
        m = 0 
        for k , v in dic1.items() :
            if v>m :
                m=v

        return len(wall) - m
                

