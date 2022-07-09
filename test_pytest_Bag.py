import random

from bag import Bag

class TestBag:

    def setup(self):
        self.bag = Bag()

    def test_init(self):
        num = random.randint(1, 90)
        assert type(self.bag.nums) == list
        assert len(self.bag.nums) == 90
        assert num in self.bag.nums

    def test_len(self):
        assert len(self.bag) == 90

    def test_choice(self):
        nums = random.sample(range(1, 91), 90)
        assert self.bag.choise() in nums
        assert self.bag.choise() not in self.bag.nums
