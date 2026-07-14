class Solution:
    def fourSum(self, nums, target):
        """
        Find all unique quadruplets that sum to target.
        Time: O(n³), Space: O(1)
        """
        # Edge case
        if len(nums) < 4:
            return []
        
        # Step 1: Sort the array
        nums.sort()
        result = []
        n = len(nums)
        
        # Step 2: First loop - fix first number
        for i in range(n - 3):
            # Optimization: if smallest 4 numbers sum > target, break
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            
            # Optimization: if largest 4 numbers sum < target, continue
            if nums[n-3] + nums[n-2] + nums[n-1] + nums[i] < target:
                continue
            
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Step 3: Second loop - fix second number
            for j in range(i + 1, n - 2):
                # Similar optimizations
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                
                # Skip duplicates for second number
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # Step 4: Two pointers for remaining two numbers
                left = j + 1
                right = n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        # Found a quadruplet!
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for left pointer
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for right pointer
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move both pointers
                        left += 1
                        right -= 1
                    
                    elif current_sum < target:
                        # Need bigger sum, move left pointer right
                        left += 1
                    
                    else:
                        # Need smaller sum, move right pointer left
                        right -= 1
        
        return result
        