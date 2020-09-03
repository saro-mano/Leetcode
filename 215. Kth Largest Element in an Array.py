import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #heapq is always min heap 
        heapq.heapify(nums)
        #kth largest element is equal to remove n-k smallest element.
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        return nums[0]
        
        
        
        
        