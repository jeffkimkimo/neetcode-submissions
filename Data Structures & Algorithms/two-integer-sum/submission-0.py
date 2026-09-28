class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct={}
        for i in range(len(nums)):
            other=target-nums[i]
            if other in dct:
                return [dct[other],i ]
            else:
                dct[nums[i]]=i

        