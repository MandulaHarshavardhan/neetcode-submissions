class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # a=[]
        # l=0
        # r=k-1
        # while r < len(nums):
        #     if r-l+1==k:
        #         a.append(max(nums[l:r+1]))
        #     l+=1
        #     r+=1
        # return a
        output=[]
        q=collections.deque()
        l=r=0
        while r < len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output