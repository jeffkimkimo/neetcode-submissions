class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num
            if need not in seen:
                seen[num] = i
            else:
                return [seen[need], i]
        