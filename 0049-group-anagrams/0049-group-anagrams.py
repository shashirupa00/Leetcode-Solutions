class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        - only lower case
        - diff length of string are possible
        - can have repeating characters
        - ordering of the groups doesn't matter

        - no empty strings

        input -> list of strings: List[str]
        output -> list of list of strings: List[List[str]]

        {(anagram) -> [list of words]}
        '''

        hashMap = defaultdict(list)
        res = []

        for word in strs:
            key = [char for char in word]
            hashMap[tuple(sorted(key))].append(word)
        
        return [list(value) for value in hashMap.values()]