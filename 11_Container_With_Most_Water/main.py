class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        area = 0

        left = 0
        right = len(height) - 1

        while left != right:
            area = min(height[left],height[right]) * (right - left)
            if max_area < area:
                max_area = area

            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1

        return max_area

height = [1,8,6,2,5,4,8,3,7]
solution = Solution
print(solution.maxArea(solution, height))