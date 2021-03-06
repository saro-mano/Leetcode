class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums)
        
        dp = [0] * l
        dp[0],dp[1] = nums[0],max(nums[0],nums[1])
        
        for i in range(2,l):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        print(dp)
        
        return dp[-1]
        