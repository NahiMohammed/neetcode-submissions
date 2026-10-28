class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = {}
        st = []

        for i, c in enumerate(s):
            if c == "(":
                st.append(i)
            elif c == ")":
                j = st.pop()
                pair[i] = j
                pair[j] = i

        res = []
        i = 0
        direction = 1

        while i < n:
            if s[i] == "(" or s[i] == ")":
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])

            i += direction

        return "".join(res)