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
                continue
            else:
                if current == []:
                    return False
                if hm[current[-1]] == s[i]:
                    current.pop(-1)
                else: 
                    return False
            print(current)
        return True if current == [] else False

            
            
