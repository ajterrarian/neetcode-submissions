class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            sorted_key = "".join(sorted(word))
            hashmap.setdefault(sorted_key, []).append(word)

        return list(hashmap.values())