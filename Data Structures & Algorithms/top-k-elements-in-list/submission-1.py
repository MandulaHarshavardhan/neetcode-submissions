class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dici={}
        li=[]
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        for key,value in sorted(dici.items(), key=lambda x: x[1], reverse=True):
            
            li.append(key)
            if len(li) == k:
                break
        return li  