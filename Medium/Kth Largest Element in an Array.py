import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k

        left=0
        right= len(nums)-1
        
        while left<= right:
            pivot_ind= random.randint(left,right)
            pivot= nums[pivot_ind]
            l=left
            r=right
            while l<=r:
                while nums[l]< pivot: l+=1
                while nums[r]> pivot: r -=1

                if l <= r:
                    nums[l],nums[r]=nums[r],nums[l]
                    l+=1
                    r -=1

            if k<=r:
                right=r
            elif k >= l :
                left= l
            else:
                return nums[k]