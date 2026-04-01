class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        numm=set(nums)
        longest = 0

        for n in numm:
            if (n - 1) not in numm: 
                length = 0
                while (n+length) in numm: 
                    length +=1 
                    longest = max(longest,length) 

        return longest

