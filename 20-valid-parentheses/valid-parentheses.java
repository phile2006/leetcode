import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> st = new ArrayDeque<>();
        Map<Character, Character> other = new HashMap<>();
        other.put('}', '{');
        other.put(')', '(');
        other.put(']', '[');

        for(char c: s.toCharArray()) {
            if(c == '{' || c == '(' || c == '['){
                st.push(c);
            }else{
                if (st.isEmpty()) {
                    return false;
                }
                char val = st.pop();
                if(val != other.get(c)) {
                    return false;
                }
            }
        }
        if (st.size() != 0) {
            return false;
        }else{
            return true;
        }
    }
}