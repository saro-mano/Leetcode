class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rightmost_char = {c:i for i,c in enumerate(S)}
        '''{'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
'''
        right = 0
        left = 0
        res = []
        for i,c in enumerate(S):
            right = max(right,rightmost_char[c])
            if i == right:
                res.append(right-left+1)
                left = right + 1
        return res
                             
            