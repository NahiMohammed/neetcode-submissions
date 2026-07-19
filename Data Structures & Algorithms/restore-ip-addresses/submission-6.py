class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []

        def valid(part):
            if len(part) > 3:
                return False
            
            if part[0] == "0" and len(part) > 1:
                return False
            
            if int(part) > 255:
                return False
            
            return True


        def backtracking(start, parts):

            # On a trouvé 4 morceaux
            if len(parts) == 4:
                if start == len(s):
                    res.append(".".join(parts))
                return


            # essayer les tailles 1,2,3
            for end in range(start+1, min(start+4, len(s)+1)):

                part = s[start:end]

                if valid(part):
                    backtracking(
                        end,
                        parts+[part]
                    )


        backtracking(0, [])

        return res