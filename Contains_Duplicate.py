class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
        for v in dict1.values():
            if v >= 2:
                return True
        return False