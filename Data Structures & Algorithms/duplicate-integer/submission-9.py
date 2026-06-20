class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if seen.get(i) != None:
                return True
            seen[i] = 1
        return False