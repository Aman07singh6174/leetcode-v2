class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            prod = 1
            g = 0
            l = 1

            for j in range(i, len(nums)):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = l * nums[j] // gcd(l, nums[j])

                if prod == g * l:
                    ans = max(ans, j - i + 1)

        return ans