class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def is_sub(a, b):
            if len(a) > len(b):
                return False

            for i in range(len(b) - len(a) + 1):
                match = True
                for j in range(len(a)):
                    if b[i + j] != a[j]:
                        match = False
                        break
                if match:
                    return True
            return False

        res = set()

        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and is_sub(words[i], words[j]):
                    res.add(words[i])

        return list(res)