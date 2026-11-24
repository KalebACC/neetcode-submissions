class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for index, num in enumerate(nums):
            searching = target-num

            if searching in seen:
                return [seen[searching],index]
            
            seen[num] = index

        return [-1,-1] 