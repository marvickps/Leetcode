class Solution {
  int maxProfit(List<int> prices) {
    int len = prices.length;
    int l=0,r=1;
    int tempMax = 0;
    // 3, 8, 1, 10,9
    while (r<len){
      if (prices[l]<prices[r]) {
        tempMax = max(tempMax, prices[r] - prices[l]); //6,
      }else{
        l=r;
      }
    r+=1;

    }
    return tempMax;
  }
}