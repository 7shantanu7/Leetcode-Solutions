class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length==0){
            return 0;
        }
        int low = prices[0];
        int profit = 0;
        for(int i=0;i<prices.length;i++){
            if(prices[i]<low){
                low = prices[i];
            }
            if(prices[i]-low>profit){
                profit=prices[i]-low;
            }
        }
        return profit;
    }
}