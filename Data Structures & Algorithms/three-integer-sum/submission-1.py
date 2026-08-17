class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        triplets = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            if nums[i] == nums[i-1] and i > 0:
                continue

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]

                if three_sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif three_sum > 0:
                    k -= 1

                elif three_sum < 0:
                    j += 1

        return triplets
