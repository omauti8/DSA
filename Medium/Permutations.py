class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        set=[False]*len(nums)
        def back(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if set[i]:
                    continue
                set[i]= True
                path.append(nums[i])
                back(path)

                path.pop()
                set[i]= False
        
        back([])
        return ans