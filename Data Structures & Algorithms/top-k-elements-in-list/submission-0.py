class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq_pair = []
        final_res = []
        for n in nums:
            res[n] = res.get(n, 0) + 1

        for n, cnt in res.items():
            freq_pair.append([cnt, n])

        freq_pair.sort()

        while len(final_res) < k:
            final_res.append(freq_pair.pop()[1])

        return final_res
        