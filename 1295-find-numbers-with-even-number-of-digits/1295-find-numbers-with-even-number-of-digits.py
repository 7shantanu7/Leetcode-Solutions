class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digits = 0
        def count_digits(num):
            if(num<0):
                return -1
            if(num==0):
                return 1
            count = 0
            while num>0:
                num= num//10
                count+=1
            return count
        for i in nums:
            g = count_digits(i)
            if g%2==0:
                digits+=1
        return digits
        
