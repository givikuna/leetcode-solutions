#include <vector>
using namespace std;

class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            vector<int> arr = {};
            for (int i = 0; i < nums.size(); i++) {
                if (nums[i] != val) {
                    arr.push_back(nums[i]);
                }
            }
            for (int i = 0; i < nums.size(); i++) {
                nums[i] = i < arr.size() ? arr[i] : val + 1;
            }
            return arr.size();
        }
    };
