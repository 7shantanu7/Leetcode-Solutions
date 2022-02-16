class Solution :
    def  searchRange(self, nums,  target) :
        ans = [-1, -1]
        ans[0] = self.search(nums, target, True)
        if (ans[0] != -1) :
            ans[1] = self.search(nums, target, False)
        return ans
    def  search(self, nums,  target,  findStart):
        ans = -1
        start = 0
        end = len(nums) - 1
        while (start <= end) :
            mid = start + int((end - start) / 2)
            if (target < nums[mid]) :
                end = mid - 1
            elif(target > nums[mid]) :
                    start = mid + 1
            else :
                    #  potential ans found
                ans = mid
                if (findStart) :
                    end = mid - 1
                else :
                    start = mid + 1
        return ans