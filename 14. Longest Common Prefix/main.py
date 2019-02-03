class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if strs == []:
            return ""

        prefix = strs[0]
           
        for i in range(1, len(strs)):
            j = 0
            while j < len(strs[i]) and j < len(prefix):
                if strs[i][j] == prefix[j]:
                    j += 1
                else:
                    prefix = prefix[:j]
                    break
            if j == len(strs[i]):
                prefix = strs[i]

        return prefix

if __name__ == "__main__":
    strs = []

    solution = Solution()
    print(solution.longestCommonPrefix(strs))