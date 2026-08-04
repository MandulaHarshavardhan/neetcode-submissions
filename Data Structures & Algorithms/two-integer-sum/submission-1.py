class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dici={}
        for i,v in enumerate(nums):
            diff=target-v
            if diff in dici:
                return [dici[diff],i]  
            dici[v]=i
        return         