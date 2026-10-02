class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has_sortedWord = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in has_sortedWord:
                has_sortedWord[sortedWord].append(word)
            else:
                has_sortedWord[sortedWord] = [word]
        return list(has_sortedWord.values())