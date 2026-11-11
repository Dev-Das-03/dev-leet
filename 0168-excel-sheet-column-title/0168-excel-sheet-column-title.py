class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = ""
        while columnNumber > 0:
            if columnNumber > 26:
                if columnNumber % 26 == 0:
                    c = (columnNumber % 26) + 90
                    a = chr(c) + a
                    columnNumber = (columnNumber // 26) - 1
                else:
                    c = (columnNumber % 26) + 64
                    a = chr(c) + a
                    columnNumber //= 26
            elif columnNumber <= 26:
                c = columnNumber + 64
                a = chr(c) + a
                columnNumber //= 26
                break
        return a