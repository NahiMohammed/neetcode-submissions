class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []

        for c in s:
            if st and st[-1][0] == c:
                char, count = st[-1]
                st[-1] = (char, count + 1)
            else:
                st.append((c, 1))

            if st[-1][1] == k:
                st.pop()

        return "".join(c * count for c, count in st)