class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        use=[False]* len(nums)

        def back(path):
            if len(path)== len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if use[i]:
                    continue

                if i>0 and nums[i]== nums[i-1] and not use[i-1]:
                    continue
                
                use[i]= True
                path.append(nums[i])
                back(path)

                path.pop()
                use[i]= False
        back([])
        return res
