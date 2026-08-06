class Dict:
    def __init__(self):
        self.items = [None] * 8


    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = (key, value)


    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


# 해시 충돌 가능
my_dict = Dict()
my_dict.put("333", 7)
my_dict.put("77", 6)
print(my_dict.get("333"))
print(my_dict.get("77"))
print(my_dict.get("333"))
