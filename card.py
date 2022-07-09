import random

class Card:
    def __init__(self, nums):
        self.nums = nums # random.sample(range(1, 91), 15)
        # self.name = name
        self.data = []
        for i in range(0, 3):
            tmp = sorted(self.nums[5 * i: 5 * (i + 1)])
            for j in range(0, 4):
                index = random.randint(0, len(tmp))
                tmp.insert(index, 0)
            self.data += tmp

    def __str__(self):
        heading = '-' * 26 + '\n'
        card_string = ''
        for index, i in enumerate(self.data):
            if len(str(i)) == 2:
                card_string += f'{str(i)}'
            elif len(str(i)) == 1:
                if i == 0:
                    card_string += f'  '
                else:
                    card_string += f' {str(i)}'
            if index == 8 or index == 17:
                card_string += '\n'
            else:
                card_string += ' '
        ending = '\n' + '-' * 26
        return heading + card_string + ending

    def __contains__(self, item):
        return item in self.data

    def del_num(self, num):
        # if num not in self.data:
        #     return f'Числа нет в карточке'
        if num in self.data:
            self.data[self.data.index(num)] = ' -'

    def check_end(self):
        return set(self.data) == {0, ' -'}

# if __name__ == '__main__':
#     nums = random.sample(range(1, 91), 20)
#     a = Card([1,2,3])
#     print(a.data)