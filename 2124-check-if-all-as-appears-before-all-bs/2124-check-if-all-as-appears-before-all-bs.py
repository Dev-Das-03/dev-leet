class Solution:
    def checkString(self, s: str) -> bool:
        x = 0
        for i in range(len(s)):
            if s[i] == "a":
                x = i
        if ("a" not in s) or ("b" not in s):
            return True
        elif x < s.index("b"):
            return True
        else:
            return False