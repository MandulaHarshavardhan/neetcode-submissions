class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initialize answer array with 1's
        ans = [1] * n

        # Step 1: Store prefix products
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # Step 2: Multiply with suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans 