class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # curr=head
        seen=set()
        duplicates=set()
        # while curr:
        #     if curr.val not in seen:
        #         seen.add(curr.val)
        #     else:
        #         duplicates.add(curr.val)
        #     curr=curr.next
        # return duplicates
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                duplicates.add(i)
        for i in duplicates:
            return i
    