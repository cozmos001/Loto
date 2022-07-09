import unittest
import random
from bag import Bag


class TestBarrel(unittest.TestCase):

    def setUp(self):
        self.bag = Bag()

    def test_init(self):
        num = random.randint(1, 90)
        self.assertIsInstance(self.bag.nums, list)
        self.assertEqual(len(self.bag.nums), 90)
        self.assertIn(num, self.bag.nums)

    def test_len(self):
        self.assertEqual(len(self.bag), 90)

    def test_choice(self):
        nums = random.sample(range(1, 91), 90)
        self.assertIn(self.bag.choise(), nums)
        self.assertNotIn(self.bag.choise(), self.bag.nums)
