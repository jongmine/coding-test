class Solution {
    public double solution(int[] numbers) {
        
        float total = 0;
        
        for (int number: numbers)
            total += number;
        
        float average = total / numbers.length;
            
        return average;
    }
}