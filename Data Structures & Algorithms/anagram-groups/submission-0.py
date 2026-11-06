from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #mapping chara count to a list of words
        map = defaultdict(list)
        for str in strs:
            charlist = [0]*26
            for c in str:
                charlist[ord(c)-ord("a")]+=1
            map[tuple(charlist)].append(str)
        return list(map.values())   

        

        