class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int st:stones){
            if (pq.size()>0){
                int stone=pq.peek();
                if (stone==st){
                    pq.poll();
                }else {
                    pq.offer(Math.abs(st-stone));
                }
            }else{
                pq.offer(st);
            }
        }
        if (pq.size()>0){
            return pq.peek();
        } 
        return 0 ;
        
    }
}
