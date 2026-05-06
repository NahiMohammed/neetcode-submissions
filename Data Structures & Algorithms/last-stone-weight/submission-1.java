class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int st:stones){
            pq.offer(st);
        }
        while( pq.size()>1){
            int a = pq.poll();
            int b = pq.poll();
            if (a!=b){
                pq.offer(Math.abs(a-b));
            }
        }
        if (pq.size()>0){
            return pq.peek();

        }
        return 0;
        
    }
}
