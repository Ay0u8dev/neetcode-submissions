class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in numbers:
            x = target - n
            if x in numbers:
                return [numbers.index(n)+1, numbers.index(x)+1]
        return [] 