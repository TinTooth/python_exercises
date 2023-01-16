


class Solution(object):

    def __init__(self, nums):
       self.nums = nums

    def searchRange(self,target):
        l = 0
        r = len(self.nums)-1

        while l < r:
            mid = (l+r)//2
            if self.nums[mid] < target:
                l = mid+1
            elif self.nums[mid] == target:
                r = mid
            else:
                r = mid-1

        if self.nums[l] != target:
            return [-1,-1]
        else:
            start = l
            r = len(self.nums) -1

            while l <=r:
                mid = (l+r)//2
                if self.nums[mid] == target:
                    l = mid + 1
                else:
                    r = mid - 1
            
        return [start,r]
        
            


        
        
    def find_lower(self,target):
        start = 0
        end = len(self.nums)-1
        mid = (start+end)//2 



        return mid

    def find_upper(self,target):
        pass 