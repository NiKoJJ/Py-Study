# Card Module
class Ture(object):
    pass


# Card 类
class Card():
    """ A Playing Card
    """
    RANKS = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['梅', '方', '红', '黑']

    def __init__(self, rank, suit, face_up=Ture):  # 初始化
        self.rank = rank  # 牌面数字
        self.suit = suit  # 花色
        self.is_face_up = face_up  # 正面

    def __str__(self):  # 牌信息
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = 'XX'
        return rep

    def pic_order(self):  # 牌序号
        if self.rank == 'A':
            facenum = 1
        elif self.rank == 'J':
            facenum = 11
        elif self.rank == 'Q':
            facenum = 12
        elif self.rank == 'K':
            facenum = 13
        else:
            facenum = int(self.rank)

        if self.suit == '梅':
            Suit = 1
        elif self.suit == '方':
            Suit = 2
        elif self.suit == '红':
            Suit = 3
        else:
            Suit = 4
        return (Suit - 1) * 13 + facenum

    def flip(self):  # 翻牌方法
        self.is_face_up = not self.is_face_up


# Hand 类
class Hand():  # 牌手
    def __init__(self):
        self.cards = []  # 列表变量存放牌手的牌

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) +" "+"\t"  # \t横向制表符
        else:
            rep = '无牌'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


# poke 类
class Poke(Hand):  # 继承Hand
    def populate(self):  # 生成一副牌
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):  # 洗牌
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=13):  # 发牌 13张/人
        for round in range(per_hand):
            for hand in hands:
                if self.cards:

                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                else:
                    print('不能继续发牌，牌已发完！')


if __name__ == "__main__":
    print('扑克小游戏')
    player = [Hand(), Hand(), Hand(), Hand()]
    pokel = Poke()
    pokel.populate()
    pokel.shuffle()
    pokel.deal(player, 13)
    n = 1
    for hand in player:
        print('牌手', n, end=':')
        print(hand)
        n = n + 1
    input('\n Press the enter key to exit.')
