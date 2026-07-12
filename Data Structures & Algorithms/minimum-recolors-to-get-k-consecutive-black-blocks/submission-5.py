class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = len(blocks)
        curr = 0
        L = 0

        for R in range(len(blocks)):
            if blocks[R] == "W":
                curr += 1

            if R - L + 1 > k:
                if blocks[L] == "W":
                    curr -= 1
                L += 1

            if R - L + 1 == k:
                res = min(res, curr)

        return res