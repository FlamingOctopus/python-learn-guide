class MyDict(dict):
    def get(self, key):
        if key not in self.keys():
            print(0)
        else:
            print(super().get(key))


my_dict = MyDict()
my_dict["test"] = "test"
my_dict.get("test")
my_dict.get(1)
