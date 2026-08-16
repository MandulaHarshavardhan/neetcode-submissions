class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        a=set()
        l=0
        ans=0
        for i in range(n):
            while s[i] in a:
                a.remove(s[l])
                l+=1
            a.add(s[i])
            ans=max(ans,i-l+1)
        return ans