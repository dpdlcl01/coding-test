"""
K번째수

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를
배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
array의 길이는 1 이상 100 이하입니다.
array의 각 원소는 1 이상 100 이하입니다.
commands의 길이는 1 이상 50 이하입니다.
commands의 각 원소는 길이가 3입니다.


Java
import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for (int i = 0; i < commands.length; i++) {
            int start = commands[i][0];  // i
            int end = commands[i][1];    // j
            int k = commands[i][2];      // k

            // 1. 배열 자르기 (Arrays.copyOfRange는 끝 인덱스는 미포함)
            int[] temp = Arrays.copyOfRange(array, start - 1, end);

            // 2. 정렬
            Arrays.sort(temp);

            // 3. k번째 값 추출 (1-based index → k-1)
            answer[i] = temp[k - 1];
        }

        return answer;
    }
}
"""
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        # 1. 배열 자르기 (주의: 인덱스는 0부터 시작 → i-1 ~ j)
        sliced = array[i-1:j]
        # 2. 정렬
        sliced.sort()
        # 3. k번째 요소 (주의: k번째는 1-based index → k-1)
        answer.append(sliced[k-1])
    return answer

# test
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))