class Solution:
    def countOfAtoms(self, formula: str) -> str:
        st = []
        idx = 0 
        while idx <len(formula) :
            caracter = formula[idx]
            if caracter == ")":
                idx += 1
                num = ""

                while idx < len(formula) and formula[idx].isdigit():
                    num += formula[idx]
                    idx += 1

                l = []
                while st and st[-1] != "(":
                    l.append(st.pop())
                st.pop()
                s = "".join(reversed(l))
                mult = int(num) if num else 1

                cnt = defaultdict(int)
                j = 0
                while j < len(s):
                    el = s[j]
                    j += 1
                    while j < len(s) and s[j].islower():
                        el += s[j]
                        j += 1
                    k = ""
                    while j < len(s) and s[j].isdigit():
                        k += s[j]
                        j += 1
                    cnt[el] += int(k) if k else 1

                for el, c in cnt.items():
                    st.extend(el + str(c * mult))

            else :
                st.append(caracter)
                idx+=1
        
        freq = defaultdict(int)

        i = 0
        while i < len(st):
            if st[i].isupper():
                element = st[i]
                i += 1

                while i < len(st) and st[i].islower():
                    element += st[i]
                    i += 1

                num = ""
                while i < len(st) and st[i].isdigit():
                    num += st[i]
                    i += 1

                freq[element] += int(num) if num else 1
            else:
                i += 1
        res = ""

        for element in sorted(freq):
            res += element
            if freq[element] > 1:
                res += str(freq[element])

        return res