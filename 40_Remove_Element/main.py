class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        try:
            i = 0
            while True:
                if len(nums) <= i:
                    break
                if nums[i] == val:
                    del nums[i]
                    continue    
                i += 1
        except Exception as e:
            print(e)

        return len(nums)

if __name__ == "__main__":
    nums = [3,2,2,3]
    solution = Solution()
    print(solution.removeElement(nums, 3))
