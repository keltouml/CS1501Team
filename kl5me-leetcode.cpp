Keltoum Laghjibi
kl5me

class Solution {
public:
    int num = 0;
    int reverse (int var) {
        while (var != 0) {
            int x = var % 10;
            var /= 10;
            if (num > INT_MAX/10 || (num == INT_MAX / 10 && x > 7)) {
                return 0;
            }
                
            if (num < INT_MIN/10 || (num == INT_MIN / 10 && x < -8)) {
                return 0;
            }
            num = num * 10 + x;
        }
        return num;
    }
};