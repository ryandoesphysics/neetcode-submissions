class Solution:

    def encode(self, strs: List[str]) -> str:
        self.d = {i:str(v) for i, v in enumerate(strs)}
        encoded_string = str(''.join(strs))
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_string = [self.d.get(i) for i in self.d.keys()]
        return decoded_string