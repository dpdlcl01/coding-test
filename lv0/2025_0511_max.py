"""
최댓값 만들기 (1)

정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

제한사항
0 ≤ numbers의 원소 ≤ 10,000
2 ≤ numbers의 길이 ≤ 100

Java
class Solution {
    public int solution(int[] numbers) {

        int max = 0;

        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                int n = numbers[i] * numbers[j];
                if (n > max) {
                    max = n;
                }
            }
        }

        return max;
    }
}
"""

def solution(numbers):
    max = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            n = numbers[i] * numbers[j]
            if n > max:
                max = n

    return max


# test
print(solution([3, 4, 5, 6, 7])) # 42