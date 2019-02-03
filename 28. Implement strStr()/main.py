class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return is
            
        return -1

if __name__ == "__main__":
    haystack = "hello" 
    needle = "ll"
    solution = Solution()
    print(solution.strStr(haystack,needle))
