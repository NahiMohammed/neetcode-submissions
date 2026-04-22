

class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (!map.containsKey(c)) {
                stack.addLast(c);
            } else {
                if (stack.isEmpty() || stack.removeLast() != map.get(c)) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}