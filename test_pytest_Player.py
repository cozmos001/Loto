from player import PlayerCPU
from card import Card


class TestPlayerCPU:

    def setup(self):
        self.card = Card([1, 2, 3])
        self.name = 'Alex'
        self.playerCPU = PlayerCPU(self.name, self.card)

    def test_init(self):
        assert self.playerCPU.name == 'Alex'
        assert self.playerCPU.card == self.card
        assert self.playerCPU.win is None

    def test_step(self):
        self.playerCPU.step(1)
        assert self.playerCPU.win is None
        self.playerCPU.step(2)
        assert self.playerCPU.win is None
        self.playerCPU.step(3)
        assert self.playerCPU.win is True
