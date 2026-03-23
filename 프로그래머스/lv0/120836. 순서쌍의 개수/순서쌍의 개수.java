class Solution {
	public int solution(int n) {
		int answer = 0;

        // 약수는 쌍으로 존재하므로 중간 숫자까지 확인하면 나머지는 자동으로 계산할 수 있다.
		for (int i = 1; i * i <= n; i++) 
			if (n % i == 0)
                // x == y : 한 번만 추가
                if (i *i == n)
                    answer++;
                // x != y : 두 번 추가
                else 
                    answer += 2;
		return answer;
    }
}
