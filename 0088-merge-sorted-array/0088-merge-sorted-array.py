class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m < len(nums1):
            nums1.pop(m)
        while n < len(nums2):
            nums2.pop(n)
        for k in range(n):
            nums1.append(nums2[k])
        nums1.sort()