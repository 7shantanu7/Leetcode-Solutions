class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        list = []
        for i in nums:
            if(nums[abs(i)-1])<0:
                list.append(abs(i))
            else:
                nums[abs(i)-1]*=-1
        return list