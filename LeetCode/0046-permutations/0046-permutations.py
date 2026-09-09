# import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # 1. itertools 사용
        # perm_object = itertools.permutations(nums)
        # answer = list(map(list, perm_object))
        
        # 2. backtracking
        answer = []
        visited = [False] * len(nums)

        n = len(nums)
        r = n # 모든 원소를 사용하므로 r = n

        def backtrack(path):
            # r개를 선택하면 순열 하나 완성
            if len(path) == r:
                answer.append(path[:])
                return

            # 현재 자리에 넣을 숫자 선택
            for i in range(len(nums)):
                # 이미 사용한 숫자 제외
                if visited[i]:
                    continue

                # 선택
                path.append(nums[i])
                visited[i] = True

                # 다음 자리 선택
                backtrack(path)

                # 선택 취소
                path.pop()
                visited[i] = False
            
        backtrack([])
        return answer