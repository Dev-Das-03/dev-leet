class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] == 9:
            digits.insert(0,0)

        for i in range(1,len(digits)+1):
            if digits[-i] == 9:
                digits[-i] = 0
            else:
                digits[-i] += 1
                break
                
        if digits[0] == 0:
            digits.pop(0)

        return digits
