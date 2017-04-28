class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        try:
            while True:
                nums.remove(val)
        except:
            return len(nums)

print Solution().removeElement([3, 2, 2, 3], 3)