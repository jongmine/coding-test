import java.util.Set;
import java.util.HashSet;

class Solution {
    public int solution(String[] s1, String[] s2) {
        
        Set<String> set = new HashSet<String>();
        int answer = 0;
        
        for (String i : s1)
            set.add(i);
        for (String i : s2)
            if (set.contains(i))
                answer += 1;
            
        return answer;
    }
}