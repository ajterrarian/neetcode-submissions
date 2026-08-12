class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest_streak = 0

        for num in numbers:
            #check if num is start of sequence
            if (num - 1) not in numbers:
                current_num = num
                current_streak = 1

                #keep looking for consecutive numbers
                while(current_num + 1) in numbers:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak