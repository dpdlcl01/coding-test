"""
최댓값 만들기 (2)

정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

제한사항
-10,000 ≤ numbers의 원소 ≤ 10,000
2 ≤ numbers 의 길이 ≤ 100

Java
import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);  // 1. 배열을 오름차순으로 정렬
        int n = numbers.length;  // 2. 배열의 길이를 변수 n에 저장
        return Math.max(numbers[0] * numbers[1], numbers[n-1] * numbers[n-2]);  // 3. 두 가지 곱 중 큰 값 반환
    }
}
"""

def solution(numbers):

    # 배열을 오름차순 정렬
    numbers.sort()

    # 가장 큰 두 수의 곱 vs 가장 작은 두 수(음수일 수 있음)의 곱 비교
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])


# test
print(solution([3, 4, 5, 6, -7])) # 30