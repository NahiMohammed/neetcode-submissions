class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        sub = []

        def backtracking(start):
            remaining_chars = len(s) - start
            remaining_segments = 4 - len(sub)

            # Prune impossible branches
            if remaining_chars < remaining_segments:
                return
            if remaining_chars > remaining_segments * 3:
                return

            if start == len(s):
                if len(sub) == 4:
                    res.append(".".join(sub))
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]

                if len(segment) > 1 and segment[0] == "0":
                    break

                if int(segment) > 255:
                    break

                sub.append(segment)
                backtracking(end)
                sub.pop()

        if not 4 <= len(s) <= 12:
            return []

        backtracking(0)
        return res