class Solution {
    public int calPoints(String[] operations) {
        Deque<Integer> st = new ArrayDeque<>();

        for (String s : operations) {
            if (s.equals("+")) {
                int last = st.pop();
                int second = st.peek();

                st.push(last);
                st.push(last + second);

            } else if (s.equals("D")) {
                st.push(st.peek() * 2);

            } else if (s.equals("C")) {
                st.pop();

            } else {
                st.push(Integer.parseInt(s));
            }
        }

        int sum = 0;
        for (int val : st) sum += val;

        return sum;
    }
}