class Solution {
    public boolean canFinish(int n, int[][] p) {
        int a[]=new int[n];
        List<List<Integer>> li=new ArrayList<>();
        for(int i=0;i<n;i++)
        {
            li.add(new ArrayList<>());
        }
        for(int i=0;i<p.length;i++)
        {
            li.get(p[i][1]).add(p[i][0]);
        }
        for(int i=0;i<n;i++)
        {
            if(!func(li,a,i))
                return false;
        }
        return true;
    }
    public boolean func(List<List<Integer>> li, int a[], int k)
    {
        if(a[k]==1)
            return true;
        if(a[k]==2)
            return false;
        a[k]=2;
        for(int i:li.get(k))
        {
            if(!func(li,a,i))
                return false;
        }
        a[k]=1;
        return true;
    }
}