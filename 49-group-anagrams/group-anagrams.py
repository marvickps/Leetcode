class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            sort = sorted(s)
            st = ''.join(sort)
            if st in dic:
                dic[st].append(s)

            else:
                dic[st] = [s]
            
        return list(dic.values())