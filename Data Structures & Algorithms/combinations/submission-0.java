class Solution {
    private List<List<Integer>> res;
    private int n;
    private  int k;
    public List<List<Integer>> combine(int n, int k) {
        this.n=n;
        this.k=k;
        res= new ArrayList<>();
        helper(new ArrayList<>(),1);
        return res;
    }
    private void helper(List<Integer> curr,int start){
        if (curr.size()==k){
            res.add(new ArrayList<>(curr));
            return ;
        }
        for (int i =start ; i<=n;i++){
            curr.add(i);
            helper(curr,i+1);
            curr.remove(curr.size()-1);
        

        }

    }
}