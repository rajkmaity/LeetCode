class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            if len(strs)==0:
                return []
            d={}
            for s in strs:
                sorted_s=sorted(s)
                sort_s=''.join(sorted_s)
                print(sort_s)
                if sort_s in d:
                    d[sort_s].append(s)
                else:
                    d[sort_s]=[]
                    d[sort_s].append(s)
            res=[]
            for key in d.keys():
                res.append(d[key])
            return res

