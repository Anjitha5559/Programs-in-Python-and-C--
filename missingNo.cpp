 class Solution{
  public:
    int missingNumber(vector<int>& array, int n) {
        int sum1 = 0;
        int sum = n*(n+1)/2;
        for(int i=0;i<array.size();i++){
         sum1 += array[i];
        }
        int missing = sum -sum1;
            return missing;

    }
};   