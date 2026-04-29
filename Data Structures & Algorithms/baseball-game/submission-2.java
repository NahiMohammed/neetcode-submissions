class Solution {
    public int calPoints(String[] operations) {
        int res = 0;
        Deque<Integer> d = new ArrayDeque<>();
        for (String s : operations) {
            if (s.equals("+")) {
                int a = d.pop();
                int b = d.pop();
                d.push(b);
                d.push(a);
                d.push(a + b);
                res = res + a + b;
            } else if (s.equals("D")) {
                int a = d.pop();

                d.push(a);
                d.push(a * 2);
                res = res + a * 2;

            } else if (s.equals("C")) {
                int a = d.pop();
                res = res - a;

            } else {
                d.push(Integer.parseInt(s));
                res = res + Integer.parseInt(s);
            }
        }
        return res;
    }
}