class Solution {
    public boolean isPalindrome(String s) {
        String s1="";
        String s2="";
        for(int i=0;i<s.length();i++){
            if(String.valueOf(String.valueOf(s.charAt(i))).toLowerCase().matches("[a-z0-9]")){
                s1+=String.valueOf(String.valueOf(s.charAt(i))).toLowerCase();
            }
        }
        for(int i=s.length()-1;i>=0;i--){
            if(String.valueOf(String.valueOf(s.charAt(i))).toLowerCase().matches("[a-z0-9]")){
                s2+=String.valueOf(String.valueOf(s.charAt(i))).toLowerCase();
            }
        }
               if(s1.equals(s2)){
                   return true;
               }
               return false;
        
    }
}