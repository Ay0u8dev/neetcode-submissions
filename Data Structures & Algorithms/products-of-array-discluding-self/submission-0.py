class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            product = 1
            for j, n in enumerate(nums):
                if i != j:
                    product *= n
            output.append(product)
        return output
            