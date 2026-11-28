class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        x = ""
        for i in range(len(words)):
            x = x + words[i][0]
        if x == s:
            return True
        else:
            return False