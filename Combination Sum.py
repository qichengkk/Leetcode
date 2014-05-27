class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.combinationSumRecur(sorted(candidates), result, [], 0, target)
        return result
        
    def combinationSumRecur(self, candidates, result, current, start, target):
        if target == 0:
            result.append(current)
        else:
            i = start
            while i < len(candidates) and candidates[i] <= target:
                self.combinationSumRecur(candidates, result, current + [candidates[i]], i, target - candidates[i])
                i += 1