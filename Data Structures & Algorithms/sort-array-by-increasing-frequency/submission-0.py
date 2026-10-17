class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number
        # Sort by ascending frequency, breaking ties by decreasing value 
        
        count = Counter(nums)
        nums.sort(key=lambda n: (count[n], -n))
        return nums
