class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(part):
            # vide
            if not part:
                return False
            if len(part)>3 :
                return False
            # > 255
            if int(part) > 255:
                return False
            # leading zero
            if len(part) > 1 and part[0] == "0":
                return False
            return True
        ##########################
        if len(s)> 12 :
            return[]
        ##########################
        res=[]
        def b(i, j, k):
            if k >= len(s):
                return

            if i < j < k < len(s):
                if valid(s[:i]) and valid(s[i:j]) and valid(s[j:k]) and valid(s[k:]):
                    res.append(s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:])
            # avancer k d'abord
            b(i, j, k + 1)

            # puis j (reset k)
            b(i, j + 1, j + 2)

            # puis i (reset j,k)
            b(i + 1, i + 2, i + 3)
            

        b(1,2,3)
        return res
        