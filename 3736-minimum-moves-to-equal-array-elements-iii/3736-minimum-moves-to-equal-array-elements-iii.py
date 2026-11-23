class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(max(nums) - i for i in nums)