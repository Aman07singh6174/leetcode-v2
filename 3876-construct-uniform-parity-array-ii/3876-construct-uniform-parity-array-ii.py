
class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        if min(nums1) % 2 == 1:
            return True

        return len(set(x % 2 for x in nums1)) == 1
