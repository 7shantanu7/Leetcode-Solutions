class Solution {
    public int maximumWealth(int[][] accounts) { 
        int ans=Integer.MIN_VALUE;
        
        for(int i=0;i<accounts.length;i++)
         {
            int temp=0;
            
            for(int j=0;j<accounts[i].length;j++)
            {
                temp=temp+accounts[i][j];
            }
            
            if(temp>ans)
            {
                ans=temp;
            }
        
        }
            
        return ans;
    }}