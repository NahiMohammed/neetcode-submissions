class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        List<List<Integer>> freq = new ArrayList<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        for (int i = 0; i < nums.length + 1; i++) {
            freq.add(new ArrayList<>());
        }

        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            int num = entry.getKey();
            int cnt = entry.getValue();

            freq.get(cnt).add(num);
        }
        int[] res = new int[k];
        int idx = 0;

        for (int i = freq.size() - 1; i > 0; i--) {
            for (int num : freq.get(i)) {
                res[idx++] = num;

                if (idx == k) {
                    return res;
                }
            }
        }

        return res;
    }
}