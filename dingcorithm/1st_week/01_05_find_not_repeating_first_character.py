# 5. 반복되지 않는 문자
# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.
# "abadabac": 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!

input = "abadabac"


# O(N)
def find_not_repeating_first_character(string):
    # 반복되는지 아닌지 판단 필요
    # string에서 알파벳의 빈도수를 찾는다.
    # O(N)
    occurrence_array = find_alphabet_occurrence_array(string)

    # 빈도수가 1인 알파벳들 중에서 어떤 알파벳이 string에서 출현하는지 찾아야 한다.
    not_repeating_character_array = []

    # 빈도수를 저장한 리스트에서 등장 빈도가 1인 알파벳들만 저장하는 리스트를 만든다.자
    # O(N)
    for index in range(len(occurrence_array)):
        alphabet_occurrence = occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord('a')))

    # string에서 가장 먼저 등장하는 알파벳 찾아서 반환한다.
    # O(N)
    for char in string:
        if char in not_repeating_character_array: # 빈도수가 1인 알파벳만 존재하는 리스트
            return char

    return "_"


# 문자열에서 알파벳이 등장하는 빈도수를 저장하는 리스트를 반환한다.
# O(N)
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
