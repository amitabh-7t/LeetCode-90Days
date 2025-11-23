class Solution:
    def twoSum(self, nums: List[int], target: int):
        seen = {} # dictionary value -> index
        for index , value in enumerate(nums): # same value for both 
            complement = target - value
            if complement in seen :
                return [seen[complement], index]
            seen[value] = index # pair of index and value 



        
        