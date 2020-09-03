class Solution:
    def reverse(self, x: int) -> int:
        if x <= -2**31 or x >= (2**31 - 1):
            return 0
        s = str(abs(x))
        numb = int(s[::-1])
        if numb <= -2**31 or numb >= (2**31 - 1):
            return 0
        if x < 0:
            return (numb * -1)
        else:
            return (numb)
        