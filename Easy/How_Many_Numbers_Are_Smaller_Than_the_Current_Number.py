class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums, reverse=True)
        smaller_count = {}
        for i in range(len(sorted_num)-1):
            current_num = sorted_num[i]
            next_num = sorted_num[i+1]
            if current_num>next_num:
                remaining_num = len(sorted_num) -(i+1)
                smaller_count[current_num] = remaining_num
        smaller_count[sorted_num[-1]]=0
        output = []
        for num in nums:
            output.append(smaller_count[num])
        return output