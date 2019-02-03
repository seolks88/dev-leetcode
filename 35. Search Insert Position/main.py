import bisect

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid 
        
        return lo




if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2
    solution = Solution()
    print(solution.searchInsert(nums, target))
