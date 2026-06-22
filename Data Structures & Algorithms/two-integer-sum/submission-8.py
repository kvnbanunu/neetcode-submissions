class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        seen = {}

        for i in range(len(nums)):
            v = nums[i]

            remainder = target - v
            if seen.get(remainder) != None:
                res.append(seen[remainder])
                res.append(i)
                return res

            seen[v] = i
        return res