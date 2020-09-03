class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict()
        for each in nums:
            if each in dic:
                dic[each] += 1
                if dic[each] >= (len(nums)//2)+1:
                    return each
            else:
                dic[each] = 1
        if len(nums) == 1:
            return nums[0]