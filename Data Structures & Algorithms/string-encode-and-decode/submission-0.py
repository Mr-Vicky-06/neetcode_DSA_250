class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ''
        for s in strs:
            encode_string += str(len(s)) + '#' + s
        return encode_string

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length_of_original_str = int(s[i:j])
            end_of_str = j + 1 + length_of_original_str

            res.append(s[j + 1:end_of_str])
            i = end_of_str

        return res