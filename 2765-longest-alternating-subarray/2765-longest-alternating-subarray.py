class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = -1  
        left = 0  

        while left < n - 1:
            if nums[left + 1] - nums[left] != 1:
                left += 1
                continue

            right = left + 1
            length = 2
            alternating = True

            while right < n - 1 and alternating:
                if (nums[right + 1] - nums[right] == 1 and (length % 2 == 1)) or \
                    (nums[right + 1] - nums[right] == -1 and (length % 2 == 0)):
                    length += 1
                    right += 1
                else:
                    alternating = False
            max_length = max(max_length, length)
            left += 1

        return max_length