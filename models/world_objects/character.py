import random
from models.skill import skill
from core.nick_generator import get_random_name


class Character:
    def __init__(self, lid = False, bon = 0):
        """

        :param lid: Лидер Гарантировано получит навык + на корабле может быть только 1 лидер, в случае если их возникает 2 то выбирается лучший
        :param bon: Добавляет характеристики к базовым 5 бонусам
        """

        self.name = get_random_name()
        self.skill = None

        point = 5 + bon

        self.lid = lid

        self.control = 1
        self.harvest = 1
        self.attack = 1
        self.survival = 1
        self.max_stamina = 1

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
                self.max_stamina += 2
            point -= 1
        self.stamina = self.max_stamina
        self.__skill_gen()





    def __skill_gen(self):
        if random.randint(1,100) == 1 or self.lid:
            if random.randint(1,100) == 1:
                self.skill = random.choice(skill['leg'])
            elif random.randint(1,1000) < 101:
                self.skill = random.choice(skill['rare'])
            else:
                self.skill = random.choice(skill['simple'])

        if self.skill == 'Боец':
            self.attack += 1
        elif self.skill == 'Мертвец':
            self.stamina = max(1,int(self.stamina/2))
            self.survival *= 2
        elif self.skill == 'Бог морей':
            self.control += 3





