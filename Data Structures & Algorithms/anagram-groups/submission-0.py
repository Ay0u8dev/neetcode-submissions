class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupes = defaultdict(list)
        for s in strs:
            sortedStr = ''.join(sorted(s))
            groupes[sortedStr].append(s)
        return list(groupes.values())
                    
