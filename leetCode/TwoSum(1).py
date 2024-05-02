class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            i = 1
            while i < len(nums):
                if(target == nums[x] + nums[i]):
                    return [x,i]
                i += 1