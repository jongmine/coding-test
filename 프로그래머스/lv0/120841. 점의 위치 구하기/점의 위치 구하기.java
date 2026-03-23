class Solution {
    public int solution(int[] dot) {
        
        int answer;
        
        if (dot[0] * dot[1] > 0)
            answer = 1; // 1, 3
        else
            answer = 2; // 2, 4
        if (dot[1] < 0)
            answer += 2;
        
        return answer;
    }
}