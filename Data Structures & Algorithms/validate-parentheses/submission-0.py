class Solution:
    def isValid(self, s: str) -> bool:
        pairs={"[":"]","{":"}","(":")"}
        res=[]

        for ch in s:
            if ch in "({[":
                res.append(ch)
            else:
                if not res:
                    return False
                if pairs[res.pop()]!=ch:
                    return False
        else:
            if len(res)==0:
                return True
            else:
                return False
            