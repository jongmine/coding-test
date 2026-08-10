def solution(nums):
    pokemon_set = set(nums)
    answer = min(len(nums) / 2,len(pokemon_set))
    return answer