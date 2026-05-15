class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_strs = {}
        for st in strs:
            sorted_s = ''.join(sorted(st))
            if sorted_s not in sort_strs:
                sort_strs[sorted_s] = [st]
            else:
        
                sort_strs[sorted_s].append(st)
        print(sort_strs)        
        return list(sort_strs.values())