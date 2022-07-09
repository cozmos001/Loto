from card import Card


class TestCard:

    def setup(self):
        self.card = Card([1, 2, 30])

    def teardown(self):
        del self.card

    def test_init(self):
        assert self.card.nums == [1, 2, 30]
        assert isinstance(self.card.data, list)
        assert len(self.card.data) == 5 * 3

    def test_str(self):
        assert isinstance(str(self.card), str)
        assert str(1) in str(self.card)

    def test_contains(self):
        assert 1 in self.card

    def test_del_num(self):
        self.card.del_num(1)
        assert 1 not in self.card
        assert ' -' in self.card

    def test_check_end(self):
        assert self.card.check_end() is False
        self.card.del_num(1)
        assert self.card.check_end() is False
        self.card.del_num(2)
        assert self.card.check_end() is False
        self.card.del_num(30)
        assert set(self.card.data) == {0, ' -'}
        assert self.card.check_end()
