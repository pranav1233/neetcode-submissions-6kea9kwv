class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sett=set()

        for items in nums:
            if items in sett:
                return items
            sett.add(items)
