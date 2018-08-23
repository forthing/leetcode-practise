'''
 two sum question
 input:numbers = [2,7,11,15],target = 9
 output:index1 = 1,index2 = 2
'''
'''
class solution(object):
    def twosum(self,numbers,target):
        '''
        :param numbers:list[int]
        :param target:int
        :return:list[int]
        '''
        hash_map={}
        for index,value in enumerate(numbers):
            hash_map[value]=index
        for index1,value in enumerate(numbers):
            if target-value in hash_map:
                index2 = hash_map[target-value]
                if index1 != index2:
                    return [index1+1,ndex2+1]
'''
class solutions(object):
    def