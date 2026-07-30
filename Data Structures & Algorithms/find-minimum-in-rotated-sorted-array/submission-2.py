class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum  = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                minimum = nums[i + 1]
        return minimum