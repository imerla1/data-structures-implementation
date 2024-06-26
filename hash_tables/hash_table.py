class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def repr_my_hashmap(self):
        for item in self.data_map:
            if item is not None:
                print(item)

    def set_item(self, key, value):
        # Let's assume we are using Separate Chaining for collision handling
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in self.data_map:
            if i is not None:
                for key in i:
                    get_key = key[0]
                    all_keys.append(get_key)

        return all_keys


hash_table = HashTable()
hash_table.set_item("name", "george")
hash_table.set_item("name", "lukas")
hash_table.set_item("age", 25)
x = hash_table.keys()
