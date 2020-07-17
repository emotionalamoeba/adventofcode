class Memory:
    def __init__(self, data):
        self.data = data.copy()
        #print("Memory loaded with {} values".format(len(self.data)))

    def load(self, data):
        self.data = data.copy()
        #print("Memory loaded with {} values".format(len(self.data)))

    def __setitem__(self, index, value):
        self.data[index] = value

    def __getitem__(self, index):
        return self.data[index]

    def dump(self):
        print(', '.join(map(str, self.data)))
