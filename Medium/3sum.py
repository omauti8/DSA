class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue

            l=i+1
            r= n-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum<0:
                    l+= 1
                elif sum>0:
                    r -=1
                else:
                    res.append([nums[i],nums[l],nums[r]])

                    while l<r and nums[l] == nums[l+1]:
                        l +=1
                    while l<r and nums[r] == nums[r-1]:
                        r -=1
                    l+=1
                    r-=1
        return res
