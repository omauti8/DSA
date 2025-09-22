class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        set =[]
        def subset(i):
            if i==len(nums):
               res.append(set[:])
               return

            set.append(nums[i])
            subset(i+1)

            set.pop()
            subset(i+1)
        subset(0)
        return res