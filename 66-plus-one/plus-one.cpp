class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int s = digits.size();
        if(digits[s-1] >= 0 && digits[s-1] <= 8) {
            digits[s-1] = digits[s-1] + 1;
        } else {
            for(int i = s - 1; i >= 0; i--) {
                if(digits[i] == 9) {
                    digits[i] = 0;
                    if(i == 0) {
                        digits.insert(digits.begin(), 1);
                    }
                } else {
                    digits[i] = digits[i] + 1;
                    break;
                }
            }
        }
        return digits;
    }
};