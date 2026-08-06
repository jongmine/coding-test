class LinkedTuple:
    def __init__(self):
        self.items = []


    def add(self, key, value):
        self.items.append((key, value))


    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())


    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value) # index 번째의 LinkedTuple


    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)


# 해시 충돌 방지
my_dict = LinkedDict()
my_dict.put("333", 3)
my_dict.put("77", 2)
print(my_dict.get("333"))
print(my_dict.get("77"))
print(my_dict.get("333"))

