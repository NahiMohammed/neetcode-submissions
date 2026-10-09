class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isnumeric():
                start = j

                while j < len(abbr) and abbr[j].isnumeric():
                    j += 1

                digit = abbr[start:j]

                if digit[0] == '0':
                    return False

                i += int(digit)

            else:
                if word[i] != abbr[j]:
                    return False

                i += 1
                j += 1

        return i == len(word) and j == len(abbr)