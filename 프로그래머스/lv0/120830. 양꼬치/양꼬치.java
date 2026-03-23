class Solution {
    public int solution(int n, int k) {
        int lamb = n * 12000;
        k -= n/10;
        int soda = k * 2000;

        return lamb + soda;
    }
}