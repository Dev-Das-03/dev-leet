class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = (len(a) - len(b)) * "0" + b
        elif len (b) > len(a):
            a = (len(b) - len(a)) * "0" + a

        a = "0" + a
        b = "0" + b

        res = ""
        car = 0
        for i in range(1,len(a)+1):
            dig = (int(a[-i]) + int(b[-i]) + car) % 2
            car = (int(a[-i]) + int(b[-i]) + car) // 2
            s = str(dig)
            res = s + res
        
        if res[0] == "0":
            return res[1::]
        else:
            return res
        
