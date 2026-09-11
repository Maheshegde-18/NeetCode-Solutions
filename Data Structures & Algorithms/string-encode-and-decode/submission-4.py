class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str=""
        for ch in strs:
            encode_str+=ch +"~"
        return encode_str
    def decode(self, s: str) -> List[str]:
        decoded_str=[]
        for word in s.split("~"):
            decoded_str.append(word)
        decoded_str.pop()
        return decoded_str

