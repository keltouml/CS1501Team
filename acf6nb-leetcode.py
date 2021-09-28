class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = (n*2) * [0]
        for x in range(n):
            ans[x], ans[n + x] = nums[x], nums[x]       
        return ans