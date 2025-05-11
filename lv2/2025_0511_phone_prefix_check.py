"""
전화번호 목록

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.

Java
import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {

        // 1. 전화번호를 정렬
        Arrays.sort(phone_book);

        // 2. 인접한 요소끼리만 접두어인지 확인 (정렬했기 때문에 가능한 방식)
        for (int i = 0; i < phone_book.length - 1; i++) {
            // 다음 번호가 현재 번호의 접두어인지 확인
            if (phone_book[i + 1].startsWith(phone_book[i])) {
                return false;
            }
        }

        return true;
    }
}
"""
def solution(phone_book):
    # 1. 사전순 정렬
    phone_book.sort()

    # 2. 인접한 번호끼리만 접두어인지 확인
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True

# test
print(solution(["119", "97674223", "1195524421"])) # false