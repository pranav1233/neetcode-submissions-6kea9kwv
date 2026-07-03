class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in sett:
                lenght = 0
                while(n+lenght) in sett:
                    lenght+=1
                longest=max(longest,lenght)

        return longest
            