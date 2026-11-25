class Solution:
    def findMin(self, nums: List[int]) -> int:
        #A rotation is a circular shift right
        #Typical binary goes center and then moves from there
        left = 0
        right = len(nums)-1

        while left != right:
            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[left]
        