class Solution:
    def func(self,x):
        print(x)
        
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # print(sorted(people,key = lambda x:x[0],reverse = True))
        people.sort(key = lambda x: (-x[0],x[1]))
        '''negative sign is used to denote descending order'''
        # print(people)
        result = []
        for i in people:
            result.insert(i[1],i)
        return result
            
        