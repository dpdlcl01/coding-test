"""
가장 큰 수 찾기
제출 내역
문제 설명
정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

제한사항
1 ≤ array의 길이 ≤ 100
0 ≤ array 원소 ≤ 1,000
array에 중복된 숫자는 없습니다.

Java
import java.util.Arrays;

class Solution {
    public int[] solution(int[] array) {

        /*
        int len = array.length; // 배열의 길이
        Arrays.sort(array); // 오름차순 정렬

        int[] answer = {array[len-1], len-1};
        return answer;
        무심코 이렇게 했는데 이건 오름차순 정렬이 된 이후의 인덱스이다.
        */

        int max = array[0]; // 최댓값에 일단 첫 번째 값 저장
        int index = 0; // 인덱스

        for(int i = 1; i < array.length; i++){
            if(array[i] > max){ // 만약 i번째 값이 max보다 크면
                max = array[i];
                index = i;
            }
        }

        int[] answer = {max, index};
        return answer;
    }
}
"""

"""
자바랑 비슷하게 푼 방식
def solution(array):

    max = array[0]
    index = 0

    for i in range(1, len(array)):
        if array[i] > max:
            max = array[i]
            index = i

    answer = [max, index]
    return answer
"""
def solution(array):

    value = max(array)

    answer = [value, array.index(value)]
    return answer

# 파이썬 자체에 내장된 max, index 함수를 활용

# test
print(solution([3, 4, 5, 6, -7])) # [6, 3]