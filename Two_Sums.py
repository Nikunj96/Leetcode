class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i, nums in enumerate(nums):
            difference = target - nums
            if difference in dict1:
                return[dict1[difference], i]
            dict1[nums] = i
        return[]