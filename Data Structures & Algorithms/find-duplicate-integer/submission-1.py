class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen=set()
        # duplicates=set()
        # for i in nums:
        #     if i not in seen:
        #         seen.add(i)
        #     else:
        #         duplicates.add(i)
        # for i in duplicates:
        #     return i
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow
    