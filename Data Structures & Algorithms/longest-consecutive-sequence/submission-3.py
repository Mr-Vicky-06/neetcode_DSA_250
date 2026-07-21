class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = sorted(set(nums))
        if len(seq) == 0:
            return 0
        count = 1
        max_count = 1
        for i in range(len(seq) - 1):
            if seq[i + 1] - seq[i] == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
        return max_count