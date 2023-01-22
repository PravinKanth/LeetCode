class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dict=defaultdict(list)
        dum=0
        for i in words:
            dict[ord(i[0])-ord('a')].append(i)
        for j in s:
            qualified=dict[ord(j)-ord('a')]
            dict[ord(j)-ord('a')]=[]
            for k in qualified:
                if len(k)==1:
                    dum+=1
                else:
                    dict[ord(k[1])-ord('a')].append(k[1:])
        return dum