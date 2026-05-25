class Solution:
    def restoreIpAddresses(self,s):
        res = []

        def valid(part):
            # entre 0 et 255
            if int(part) > 255:
                return False

            # pas de leading zero
            if len(part) > 1 and part[0] == "0":
                return False

            return True

        n = len(s)

        for i in range(1, 4):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):

                    if k >= n:
                        continue

                    p1 = s[:i]
                    p2 = s[i:j]
                    p3 = s[j:k]
                    p4 = s[k:]

                    if all(valid(p) for p in [p1, p2, p3, p4]):
                        res.append(p1 + "." + p2 + "." + p3 + "." + p4)

        return res
