import unittest
from player import PlayerCPU, PlayerHuman
from card import Card


class TestPlayerCPU(unittest.TestCase):

    def setUp(self):
        self.card = Card([1, 2, 3])
        self.playerCPU = PlayerCPU('CPU', self.card)

    def test_unit(self):
        self.assertEqual(self.playerCPU.name, 'CPU')
        self.assertEqual(self.playerCPU.card, self.card)
        self.assertIs(self.playerCPU.win, None)

    def test_str(self):
        self.assertEqual(str(self.playerCPU), 'CPU')

    def test_eg(self):
        self.assertEqual(self.playerCPU, self.playerCPU)
        self.card = Card([1, 2, 3])
        self.playerCPU_2 = PlayerCPU('CPU_2', self.card)
        self.assertNotEqual(self.playerCPU, self.playerCPU_2)

    def test_step(self):
        self.playerCPU.step(1)
        self.assertIsNone(self.playerCPU.win)
        self.playerCPU.step(2)
        self.assertIsNone(self.playerCPU.win)
        self.playerCPU.step(3)
        self.assertTrue(self.playerCPU.win)


class TestPlayerHuman(unittest.TestCase):

    def setUp(self):
        self.card = Card([1, 2, 3])
        self.playerHuman = PlayerHuman('Alex', self.card)

    def test_init(self):
        self.assertEqual(self.playerHuman.name, 'Alex')
        self.assertEqual(self.playerHuman.card, self.card)
        self.assertIs(self.playerHuman.win, None)

    def test_step_true(self):
        self.playerHuman.step(1, 'y')
        self.assertIsNone(self.playerHuman.win)
        self.playerHuman.step(4, 'n')
        self.assertIsNone(self.playerHuman.win)
        self.playerHuman.step(2, 'y')
        self.assertIsNone(self.playerHuman.win)
        self.playerHuman.step(3, 'y')
        self.assertTrue(self.playerHuman.win)

    def test_step_false(self):
        self.playerHuman.step(3, 'n')
        self.assertFalse(self.playerHuman.win)
        self.playerHuman.step(4, 'y')
        self.assertFalse(self.playerHuman.win)
