class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early exit: if smallest remaining num > 0, no triplet can sum to 0
            if nums[i] > 0:
                break
            
            left, right = i + 1, n - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result