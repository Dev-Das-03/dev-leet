class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.append(nums1[i])
        return list(set(ans))
