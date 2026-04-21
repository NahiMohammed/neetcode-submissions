class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();
        for (String c: strs ){
            int[] occ= new int[26];
            for (int i=0; i<c.length();i++){
                occ[c.charAt(i)-'a']++;
            }
            String key = Arrays.toString(occ);
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(c);
        }
        return new ArrayList<>(res.values());
    }
}