class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        maxV = 0

        while l < r:
            if height[l] < height[r]:
                val = min(height[l], height[r]) * (r - l)
                l += 1
            else:
                val = min(height[l], height[r]) * -(l - r)
                r -= 1
            if val > maxV:
                maxV = val
        return maxV
        