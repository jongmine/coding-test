# 1. 두 링크드 리스트의 합 계산
# Q.  다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오.
#
# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# 각각 678, 354 이므로 두개의 총합
# 678 + 354 = 1032 를 반환해야 한다.
#
# 단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.

# [6] -> [7] -> [8]
# [3] -> [5] -> [4]
#
# A: 1032

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

def get_single_linked_list_sum(linked_list):
    sum = 0
    cur = linked_list.head
    while cur is not None:
        sum = sum * 10 + cur.data # 이전 합계를 * 10 한 후 이번 값을 더하기
        cur = cur.next

    return sum


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 각 링크드리스트를 순회해서 0~n번째 인덱스들의 value를 얻는다.
    # head의 value부터 10^n ~ 10^0을 곱하여 저장한다.
    # 저장한 값끼리 덧셈

    result = 0

    # linked_list_1_values = []
    # linked_list_1_cur = linked_list_1.head
    # while linked_list_1_cur is not None:
    #     linked_list_1_values.append(linked_list_1_cur.data)
    #     linked_list_1_cur = linked_list_1_cur.next
    #
    # for i in range(len(linked_list_1_values)):
    #     result += linked_list_1_values[i] * (10 ** (len(linked_list_1_values) - i - 1))
    #
    # linked_list_2_values = []
    # linked_list_2_cur = linked_list_2.head
    # while linked_list_2_cur is not None:
    #     linked_list_2_values.append(linked_list_2_cur.data)
    #     linked_list_2_cur = linked_list_2_cur.next
    # linked_list_2_cur = linked_list_2.head
    # for i in range(len(linked_list_2_values)):
    #     result += linked_list_2_values[i] * (10 ** (len(linked_list_2_values) - i - 1))

    sum_1 = get_single_linked_list_sum(linked_list_1)
    sum_2 = get_single_linked_list_sum(linked_list_2)

    result = sum_1 + sum_2
    return result


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))