class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        r = 0
        m = 1
        while(n>0):
            a = n%10
            r+=a
            m*=a
            n = n//10
        return (m-r)
                
        
        
            
        
