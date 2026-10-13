class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = set()
        unique =[]
        
        for n in nums:
            if n not in seen:
                seen.add(n)
                unique.append(n)
        nums[:len(unique)] = unique
        return len(unique)