class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

nums1 = [2, 7, 11, 15]
target1 = 9
solution = Solution()
print(solution.twoSum(nums1, target1))
