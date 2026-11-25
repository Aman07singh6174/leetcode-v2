
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:

        odd = 0
        even = 1
        total = 0
        ans = 0

        for num in arr:
            total += num

            if total % 2 == 0:
                ans += odd
                even += 1
            else:
                ans += even
                odd += 1

        return ans % (10**9 + 7)
