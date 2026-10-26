class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        j = 0
        sb = []

        while j < len(s):
            while i < len(s) and s[i] != ' ':
                i += 1

            for k in range(i - 1, j - 1, -1):
                sb.append(s[k])

            sb.append(" ")
            i += 1
            j = i

        sb.pop()
        return "".join(sb)