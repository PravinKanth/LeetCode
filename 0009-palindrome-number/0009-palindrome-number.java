class Solution {
    public boolean isPalindrome(int x) {
        String a=String.valueOf(x);
        String b="";
        for(int i=a.length()-1;i>=0;i--){
            b+=String.valueOf(a.charAt(i));
        }
        if(a.equals(b))return true;
           return false; 
        
    }
}