class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            res.append([num, i])

        res.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            curr = res[left][0] + res[right][0]
            if curr == target:
                return [min(res[left][1], res[right][1]), max(res[left][1], res[right][1])]

            if curr < target:
                left += 1

            else:
                right -= 1

        return []

                