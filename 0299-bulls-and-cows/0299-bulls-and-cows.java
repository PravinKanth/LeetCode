class Solution {
    public String getHint(String secret, String guess) {
        int a1=0;
        int b1=0;
        ArrayList<String> a=new ArrayList<>();
        ArrayList<String> b=new ArrayList<>();
        for(int i=0;i<secret.length();i++){
            if(String.valueOf(secret.charAt(i)).equals(String.valueOf(guess.charAt(i)))){
                a1++;
            }
            else{
                a.add(String.valueOf(secret.charAt(i)));
                b.add(String.valueOf(guess.charAt(i)));
            }
        }
        
        for(String i:a){
            if(b.contains(i)){
                b1++;
                b.remove(i);
            }
        }
        return a1+"A"+b1+"B";
        
        
    }
}