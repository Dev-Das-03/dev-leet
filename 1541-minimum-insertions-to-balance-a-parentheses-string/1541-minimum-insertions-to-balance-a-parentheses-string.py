class Solution:
    def minInsertions(self, s: str) -> int:
        i = 0
        o = 0
        a = 0
        while i < len(s):
            if s[i] == "(":
                o += 1
                i += 1

            elif s[i:i+2] == "))":
                if o == 0:
                    a += 1

                elif o > 0:
                    o -= 1
                
                i += 2
            
            elif s[i] == ")":
                if o > 0:
                    a += 1
                    o -= 1
                else:
                    a += 2
                    
                i += 1

        return o * 2 + a
                    



