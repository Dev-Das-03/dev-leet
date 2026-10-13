class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        marged = []
        for i in nums1:
            marged.append(i)
        for j in nums2:
            marged.append(j)
        
        marged.sort()
        x = len(marged)
        y = (x - 1)//2
        z = (x//2)

        if x % 2 == 0:
            return (marged[z-1]+marged[z])/2
        else:
            return marged[y]

        