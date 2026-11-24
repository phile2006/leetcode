import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> window = new HashSet<>();
        int maximum = 0;
        int l = 0;
        for (int r = 0; r<s.length(); r++) {
            while (window.contains(s.charAt(r))) {
                window.remove(s.charAt(l));
                l++;
            }
            window.add(s.charAt(r));
            maximum = Math.max(maximum, r - l + 1);
        }
        return maximum;
    }
}