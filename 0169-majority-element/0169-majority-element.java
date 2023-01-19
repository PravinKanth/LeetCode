class Solution {
    public int majorityElement(int[] nums) {
                Arrays.sort(nums);
        int i=nums[nums.length-1];
        int f=nums.length/2;
        int count=0;
        int ans=0;
        for(int j:nums){
            if(i!=j){
                count=0;
                i=j;
            }
            count+=1;
            if(count>f){
                ans=j;
                break;
            }

        }
return(ans);
        
    }
}