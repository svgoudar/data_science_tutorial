class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """

        words1 = list(map(lambda x : [x],words1)) 
        d = {"".join(x):all(b in "".join(x) for b in words2) for x in words1}

        return [x for x,y in d.items() if y]
        


v = ['amazon', 'apple', 'facebook', 'google', 'leetcode']
b = ["o","e"]
cl = Solution()

print(cl.wordSubsets(v,b))