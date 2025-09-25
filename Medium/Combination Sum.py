class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        def back(start,path, total):
            if total== target:
                res.append(path[:])
                return
            if total>target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                back(i,path,total+candidates[i])
                path.pop()

        back(0,[],0)
        return res