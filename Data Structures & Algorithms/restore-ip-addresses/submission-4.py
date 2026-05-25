class Solution:
    def restoreIpAddresses(self,s):
        res = []

        def valid(part):
            if len(part) == 0:
                return False
            if len(part) > 1 and part[0] == "0":
                return False
            return int(part) <= 255

        def backtrack(start, path):
            # si on a 4 morceaux et qu'on a tout utilisé
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            # essayer 1 à 3 chiffres
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                part = s[start:end]

                if valid(part):
                    backtrack(end, path + [part])

        backtrack(0, [])
        return res


        