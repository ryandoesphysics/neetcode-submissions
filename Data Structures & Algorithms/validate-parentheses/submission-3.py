class Solution:
    def isValid(self, s: str) -> bool:
        # stack: first in last out
        hm = {
         '{': '}',
         '(': ')',
         '[': ']',
        }
        current = []
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
        return True if current == [] else False

            
            
