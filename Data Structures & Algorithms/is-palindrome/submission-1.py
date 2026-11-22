class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        i = 0
        def check_alphanumeric(c: str) -> bool:
            if 65<=ord(c)<=90 or 97<=ord(c)<= 122 or 48<=ord(c)<=57:
                return True
            return False
        while left<right:
            while not check_alphanumeric(s[left]):
                left += 1
                if left == right:
                    return True
            
            l = s[left]

            while not check_alphanumeric(s[right]):
                right -= 1
                if right == left:
                    return True
            
            r = s[right]
            try:
                r = int(r)
                l = int(l)
            except ValueError:
                r = r.lower()
                l = l.lower()
            if r != l:
                return False
            left += 1
            right -= 1
        return True


            