class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper = set()
        lower = set()
        for i in word:
            if i.isupper():
                upper.add(i)
            else:
                lower.add(i)

        lower_upped = set()
        for char in lower:
            lower_upped.add(char.upper())

        result = list(upper & lower_upped)

        return len(result)
