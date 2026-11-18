### Procedure

1. Set left = 0 and right = nums.length.  
2. While left < right:
  Compute mid = left + (right - left) // 2.
  If nums[mid] < target, set left = mid + 1.
  Otherwise, set right = mid.
4. Return left.
