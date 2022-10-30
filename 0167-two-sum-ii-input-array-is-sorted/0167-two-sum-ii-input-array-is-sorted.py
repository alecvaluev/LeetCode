class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            currSume = numbers[left] + numbers[right]
            
            if currSume < target:
                left += 1
            elif currSume > target:
                right -= 1
            else:
                return [left + 1, right + 1]