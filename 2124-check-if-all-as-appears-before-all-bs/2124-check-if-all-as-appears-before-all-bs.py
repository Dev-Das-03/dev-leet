class Solution:
    def checkString(self, s: str) -> bool:
        x,y = 0,0
        for i in range(len(s)):
            if s[i] == "a":
                x = i
        for j in range(len(s)):
            if s[j] == "b":
                y = j
                break
        if ("a" not in s) or ("b" not in s):
            return True
        elif x < y:
            return True
        else:
            return False