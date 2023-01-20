class Solution {
    public int maxRotateFunction(int[] nums) {
        int a=0;
        int sum=0;
        int j=0;
        for(int i:nums)
        {
            sum+=i;
            a+=i*j;
            j+=1;
        }
        int ans=a;
        int l=nums.length;
        for(int i=l-1;i>=1;i--)
        {
            a=a+sum-(nums[i]*l);
            ans=Math.max(a,ans);
        }
        return ans;
    }
}