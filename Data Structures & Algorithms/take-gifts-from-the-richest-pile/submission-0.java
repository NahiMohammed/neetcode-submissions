class Solution {
    public long pickGifts(int[] gifts, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int g :gifts){
            pq.offer(g);
        }
        int gift ; 
        while(k!=0){
            gift = pq.poll();
            pq.offer((int) Math.sqrt(gift));
            k--;

        }
        int sum = 0;
        for (int x : pq) {
            sum += x;
        }
        return sum;


        
    }
}