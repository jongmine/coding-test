class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def backtrack(start, path):
            # k개 선택 완료
            if len(path) == k:
                answer.append(path[:])
                return

            # 현재 이후만 탐색
            for i in range(start, n + 1):
                 
                # 선택
                path.append(i)

                # 현재 선택 다음 위치부터 탐색
                backtrack(i + 1, path)

                # 선택 취소
                path.pop()

        backtrack(1, [])
        return answer


