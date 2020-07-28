class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(100):
            curr = 0
            while n != 0:
                r = n%10
                curr = curr + r**2
                n = n // 10
            n = curr
            if n == 1:
                return True
        return False
        
            
            