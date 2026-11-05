class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a,b = sentence1.split(),sentence2.split()
        if len(a) > len(b): a,b = b,a
        left = 0
        while left < len(a) and a[left] == b[left]:
            left += 1
            print(left)
        right = 0
        while right < len(a)-left and a[-1-right] == b[-1-right]: right += 1
        return left + right == len(a)
