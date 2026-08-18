class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dici={}
        for i in range(len(s1), len(s2) + 1):
            dici["".join(sorted(s2[i-len(s1):i]))]=dici.get(s2[i-len(s1):i],0)+1
        if "".join(sorted(s1)) in dici:
            return True
        return False