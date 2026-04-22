class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for ( String str : strs ) {
            sb.append(str.length()).append("#").append(str);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        ArrayList<String> arr= new ArrayList<>();
        int i=0;
        while(i<str.length()){
            int j = i ;
            while (str.charAt(j) !='#'){
                j++;
            }
            int l = Integer.parseInt(str.substring(i,j));
            String word = str.substring(j+1,j+1+l);
            arr.add(word);
            i=j+1+l;

        }
        return arr;
    }
}
