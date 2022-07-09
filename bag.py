import random


class Bag:
    def __init__(self):
        self.nums = random.sample(range(1, 91), 90)

    def __len__(self):
        return len(self.nums)

    def choise(self):
        num = random.choice(self.nums)
        self.nums.remove(num)
        return num
