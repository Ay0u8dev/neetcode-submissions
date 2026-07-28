class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        elif len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        length = 0
        max_length = 0
        print(sorted_nums)
        for i in range(len(nums) - 1):
            print(f"sorted_nums[i] : {sorted_nums[i]}, sorted_nums[i + 1] : {sorted_nums[i + 1]}, {sorted_nums[i] + 1 == sorted_nums[i + 1]}")
            if sorted_nums[i] == sorted_nums[i + 1]:
                continue
            if sorted_nums[i] + 1 == sorted_nums[i + 1]:
                length += 1
                print(f"length added : {length}")
            else:
                print(f"length not added : {length}, max_length : {max_length}")
                length = 0
            if max_length <= length:
                max_length = length
        if max_length == 0:
            return 1
        return max_length + 1

        # if nums == []:
        #     return 0
        # suite = [sorted(nums)[0]]
        # j = 0
        # for i in range(len(nums)):
        #     if suite[j] + 1 in nums:
        #         suite.append(suite[j] + 1)
        #         j += 1

        # if len(suite) == 1:
        #     return 1
        # return len(suite)