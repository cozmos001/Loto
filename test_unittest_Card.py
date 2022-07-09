import unittest

from card import Card


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card([1, 2, 30])

    def tearDown(self):
        del self.card

    def test_init(self):
        self.assertListEqual(self.card.nums, [1, 2, 30])
        self.assertIsInstance(self.card.data, list)
        self.assertEqual(len(self.card.data), 5 * 3)

    def test_str(self):
        self.assertIsInstance(str(self.card), str)
        self.assertIn(str(1), str(self.card))

    def test_contais(self):
        self.assertIn(1, self.card)

    def test_del_num(self):
        self.card.del_num(1)
        self.assertNotIn(1, self.card)
        self.assertIn(' -', self.card)

    def test_check_end(self):
        self.assertFalse(self.card.check_end())
        self.card.del_num(1)
        self.assertFalse(self.card.check_end())
        self.card.del_num(2)
        self.assertFalse(self.card.check_end())
        self.card.del_num(30)
        self.assertEqual(set(self.card.data), {0, ' -'})
        self.assertSetEqual(set(self.card.data), {0, ' -'})
        self.assertTrue(self.card.check_end())
