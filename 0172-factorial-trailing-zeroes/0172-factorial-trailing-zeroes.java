class Solution {
    public int trailingZeroes(int n) {
        int sol=0;
                while(true){
                    n/=5;
                    
                    sol+=n;
                    
            if(n<=5){
                if(n==5){
                    sol++;
                    break;
                }
                break;
            }
        }
        return sol;
    }
}