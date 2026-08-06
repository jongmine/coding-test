# Q. 오늘 수업에 많은 학생들이 참여했습니다. 단 한 명의 학생을 제외하고는 모든 학생이 출석했습니다.
# 모든 학생의 이름이 담긴 배열과 출석한 학생들의 배열이 주어질 때, 출석하지 않은 학생의 이름을 반환하시오.

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    # 1. 2중 반복문 O(N^2)
    # for student in all_array:
    #     if student not in present_array:
    #         return student

    # 2. 정렬: 정렬 이후 하나하나 원소들을 보며 존재하지 않는 학생을 찾으면 결석한 학생을 찾을 수 있음 O(NlogN)

    # 3. Dictionary, HashTable: O(N)
    students_dict = {}

    # hash table의 키값에 모든 학생을 등록
    for student in all_array: # O(N) * 1
        students_dict[student] = True

    # 출석한 학생들의 키값의 값을 제거 O(N) * 1
    for present_student in present_array:
        del students_dict[present_student]

    for key in students_dict.keys():
        return key


print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))