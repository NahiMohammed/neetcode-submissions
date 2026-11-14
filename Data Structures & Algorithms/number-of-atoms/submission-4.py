from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        st = [defaultdict(int)]
        i, n = 0, len(formula)
        while i < n:
            c = formula[i]
            if c == "(":
                st.append(defaultdict(int))
                i += 1
            elif c == ")":
                i += 1
                j = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[j:i]) if j < i else 1
                top = st.pop()
                for el, cnt in top.items():
                    st[-1][el] += cnt * mult
            else:
                j = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                el = formula[j:i]
                j = i
                while i < n and formula[i].isdigit():
                    i += 1
                st[-1][el] += int(formula[j:i]) if j < i else 1
        print(st)
        res = []
        for el in sorted(st[0]):
            res.append(el)
            if st[0][el] > 1:
                res.append(str(st[0][el]))
        return "".join(res)