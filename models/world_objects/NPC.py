import random



class npc():
    def __init__(self, lid = False, bon = 0):
        """

        :param lid: Лидер Гарантировано получит навык + на корабле может быть только 1 лидер, в случае если их возникает 2 то выбирается лучший
        :param bon: Добавляет характеристики к базовым 5 бонусам
        """

        point = 5 + bon

        self.lid = lid

        self.control = 1
        self.harvest = 1
        self.attack = 1
        self.survival = 1
        self.stamina = 1

        while point > 0:

            if random.randint(1,6) == 1:
                self.control += 1
            elif random.randint(1,5) == 1:
                self.harvest += 1
            elif random.randint(1,4) == 1:
                self.attack += 1
            elif random.randint(1,3) == 1:
                self.survival += 1
            else:
                self.stamina += 2

        self.skill = None




