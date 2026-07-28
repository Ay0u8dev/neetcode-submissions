class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        elif len(nums) == 0:
            return 0

        sorted_nums = sorted(set(nums))
        length = 0
        max_length = 0

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] + 1 == sorted_nums[i + 1]:
                length += 1
            else:
                length = 0

            if max_length <= length:
                max_length = length

        if max_length == 0:
            return 1
        return max_length + 1