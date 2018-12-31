class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
                

        print(nums)
        return j+1




solution = Solution()
nums = [1,2,3,3,4,4]
print(solution.removeDuplicates(nums))