class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        answer = []
        for i in range(len(nums)):
            x = str(nums[i])
            for i in x:
                answer.append(int(i))
        return answer