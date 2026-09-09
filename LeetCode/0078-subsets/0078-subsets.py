class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        # 부분 집합은 path가 만들어지는 모든 경우가 정답
        def backtrack(start, path):
            # 현재 path 자체가 하나의 부분집합
            answer.append(path[:])

            for i in range(start, len(nums)):
                # 선택
                path.append(nums[i])

                # 다음 원소 탐색
                backtrack(i + 1, path)

                # 선택 취소
                path.pop()
    
        backtrack(0, [])
        return answer