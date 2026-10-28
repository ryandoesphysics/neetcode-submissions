class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        n = len(s)
        i = 0
        while i < n:
            # read first number
            length = 0
            index = 0
            for x in range(4):
                if s[i + x] == "#":
                    length  = int(s[i:i+x])
                    index = x
                    break

            # s[i+x] = "#"
            # s[i+x+1] = first letter of the first word
            i += index + 1
            decoded_string.append(s[i:i+length])
            i += length 
        return decoded_string