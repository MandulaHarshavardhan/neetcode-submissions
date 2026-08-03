class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                return True
        return False         