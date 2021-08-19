class Solution:
    def reverse(self, x: int) -> int:
        sign = x>0
        r = 0
        x = abs(x)
        while(x>0):
            a = x%10
            r = (r*10)+a
            x = x//10
        if r > (2**31)-1 or r < (-2)**31:
            return 0
        else:
            return r if sign else -r