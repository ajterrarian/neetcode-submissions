class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return 'a9128321321'
        s = "a123".join(strs)
        return s

    def decode(self, s: str) -> List[str]:
        if s == 'a9128321321':
            return []
        if s == '':
            return ['']
        decoded = s.split("a123")
        return decoded

