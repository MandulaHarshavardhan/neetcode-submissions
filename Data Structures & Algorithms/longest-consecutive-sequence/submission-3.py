class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)#2,20,4,10,3,5
        longest=0
        for n in numset:#2
            if (n-1)not in numset:
                length=0
                while (n+length) in numset:
                    length+=1
                longest=max(length,longest)
        return longest        