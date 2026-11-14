class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        for c in expression:
            if c == ",":
                continue
            if c != ")":
                st.append(c)
                continue
            vals = []
            x = st.pop()
            while x != "(":
                vals.append(x)
                x = st.pop()
            op = st.pop()
            if op == "!":
                r = "f" if vals[0] == "t" else "t"
            elif op == "&":
                r = "t" if all(v == "t" for v in vals) else "f"
            else:
                r = "t" if any(v == "t" for v in vals) else "f"
            st.append(r)
        return st[0] == "t"