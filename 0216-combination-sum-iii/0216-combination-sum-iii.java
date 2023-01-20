class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        return func(n, k, 0);
    }
    
    public List<List<Integer>> func(int n, int k, int l){
        List<List<Integer>> vari2 = new ArrayList<>();
        
        if(l >= n || (k == 1 && n >= 10)) return vari2;
        if(k == 1 && n > l){
            List<Integer> vari = new ArrayList<>();
            vari.add(n);
            vari2.add(vari);
            return vari2;
        }
        
        for(int i = l + 1; i < n && i < 10; i++){
            List<List<Integer>> curr = func(n - i, k - 1, i);
            if(!curr.isEmpty()){
                for(List<Integer> ins : curr){
                    List<Integer> vari3 = new ArrayList<>();
                    vari3.add(i);
                    vari3.addAll(ins);
                    vari2.add(vari3);
                }
            }
        }
        
        return vari2;
    }
}