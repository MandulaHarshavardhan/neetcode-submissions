class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        # for l in range(len(heights)):
        #     for r in range(len(heights)):
        #         area=(r-l)*min(heights[l],heights[r])
        #         res=max(res,area)
        # return res        
        l=0
        r=len(heights)-1
        while l<r:
            area=(r-l)*min(heights[l],heights[r])
            res=max(area,res)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res        