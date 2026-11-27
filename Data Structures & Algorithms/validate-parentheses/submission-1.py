class Solution:
    def isValid(self, s: str) -> bool:
        # stack: first in last out
        hm = {
         '{': '}',
         '(': ')',
         '[': ']',
        }
        current = []
        print(hm.keys())
        for i in range(0,len(s)):
            if s[i] in hm.keys():
                current.append(s[i])
            else:
                if current == []:
                    return False
                if hm[current[-1]] == s[i]:
                    current.pop(-1)
                else: 
                    return False
        return False if current else True

            
            
