class Solution {
    public int[] plusOne(int[] digits) {
                ArrayList<Integer> arr=new ArrayList<>();

        if(digits[digits.length-1]!=9){
            for(int i=0;i< digits.length;i++){
                if(i==digits.length-1){
                    arr.add(digits[i]+1);
                }
                else{
                    arr.add(digits[i]);
                }

            }
        }
        else{
            int prev=1;
            int ans=0;
            for(int i= digits.length-1;i>=0;i--){
              ans=(digits[i]+prev)%10;
              arr.add(0,ans);
              if(ans==0 && digits[i]!=0){
                  prev=1;
              }
              else{
                  prev=0;
              }
            }
            if(ans==0){
                arr.add(0,1);
            }

        }

        int[] i=new int[arr.size()];
        for(int i1=0;i1<i.length;i1++){
            i[i1]=arr.get(i1);
        }
        return(i);
        
    }
}