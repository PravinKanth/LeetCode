class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        ArrayList<Integer> ar=new ArrayList<>();
        for(int i:nums){
            if(i>0){
                if(nums[i-1]>0){
                    nums[i-1]=nums[i-1]*(-1);
                }
            }
            else{
                int ab=Math.abs(i);
                if(nums[ab-1]>0){
                    nums[ab-1]=nums[ab-1]*(-1);
                }

            }
        }
        for(int i=1;i<=nums.length;i++){
            if(nums[i-1]>0){
                ar.add(i);
            }
        }
        return (ar);
        
    }
}