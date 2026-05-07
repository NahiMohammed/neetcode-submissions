class Solution {
    public int findJudge(int n, int[][] trust) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int i =0 ;i<trust.length;i++){
            map.put(trust[i][1], map.getOrDefault(trust[i][1], 0) + 1);
        }
        int target =trust.length;
        int j =-1;
        for (int key : map.keySet()) {
            if (map.get(key) == target) {
                j=key;
            }
        }
        if (j==-1  ){
            return -1;
        }
        for(int i =0 ;i<trust.length;i++){
            if (trust[i][0]==j){
                return -1;
            }
        }
        return j ;
        

        
    }
}