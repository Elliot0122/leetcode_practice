class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans = 0, len = height.size()-1;
        int left = 0;
        int right = len;
        int width = len;
        
        for(int i=0; i<len; i++){
            ans = max(ans, min(height[left], height[right])*width);
            if(height[left]>height[right])
                right--;
            else
                left++;
            width--;
        }
        return ans;
    }
};
