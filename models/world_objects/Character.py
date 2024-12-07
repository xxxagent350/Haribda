import random
from models.skill import skill


# Части имени
nicknames = [
    "Черный", "Красный", "Золотой", "Серебряный", "Бешеный",
    "Кровавый", "Железный", "Штормовой", "Теневой", "Дикий",
    "Грозный", "Безумный", "Хитрый", "Соленый", "Скалистый",
    "Буряной", "Огненный", "Ночной", "Грозовой", "Ледяной",
    "Яростный", "Ветряной", "Призрачный", "Лунный", "Адский",
    "Королевский", "Бесстрашный", "Светлый", "Бронзовый", "Чумной",
    "Мрачный", "Пылающий", "Песчаный", "Костяной", "Болотный",
    "Тёмный", "Буревестный", "Облачный", "Охотничий", "Снежный",
    "Молниеносный", "Солнечный", "Голодный", "Тихий", "Беспощадный",
    "Лютый", "Стальной", "Бледный", "Коварный", "Бессмертный",
    "Грозящий", "Крылатый", "Вечный", "Мертвенный", "Бушующий",
    "Духовный", "Вихревой", "Трёхглавый", "Звёздный", "Огромный",
    "Чёрствый", "Разрушительный", "Титанический", "Древний", "Водяной",
    "Горящий", "Каменный", "Роковой", "Пыльный", "Светящийся",
    "Пепельный", "Гибельный", "Морозный", "Тропический", "Лесной",
    "Холодный", "Благородный", "Медный", "Ослепительный", "Алмазный",
    "Сквозной", "Грозовой", "Чёрный", "Кристальный", "Туманный",
    "Пьянящий", "Жаркий", "Жестокий", "Зловещий", "Бурлящий"
]

# Основы
bases = [
    "Джек", "Энн", "Морган", "Крюк", "Флинт", "Ворон",
    "Клык", "Костяной", "Борода", "Рейвен", "Волк", "Карабин",
    "Шпагат", "Охотник", "Морской", "Разбойник", "Капитан",
    "Ястреб", "Змея", "Тигр", "Орел", "Таран", "Ланс",
    "Варвар", "Барон", "Дракон", "Лансер", "Кочевник",
    "Акула", "Тарантул", "Сокол", "Вождь", "Медведь",
    "Грифон", "Пират", "Гладиатор", "Всадник", "Призрак",
    "Штурман", "Гарпун", "Зверь", "Тень", "Китобой",
    "Стрелок", "Бандит", "Тюлень", "Шаман", "Сапсан",
    "Корсар", "Сокол", "Саламандра", "Чудовище", "Легионер",
    "Лев", "Палач", "Тритон", "Минотавр", "Громовержец",
    "Олень", "Странник", "Сирена", "Охотник", "Арбалетчик",
    "Бык", "Чёрт", "Зодчий", "Хищник", "Дельфин",
    "Зверолов", "Зверобой", "Мастер", "Ткач", "Гончар",
    "Сокол", "Морж", "Альбатрос", "Орлан", "Дервиш",
    "Ветер", "Летучий", "Хранитель", "Молот", "Гигант",
    "Бык", "Шип", "Змей", "Рысь", "Пастырь",
    "Моряк", "Старейшина", "Пантера", "Шторм", "Воевода"
]


def generate_pirate_name():
    nickname = random.choice(nicknames)
    base = random.choice(bases)
    return f"{nickname} {base}"


class Character:
    def __init__(self, lid = False, bon = 0):
        """

        :param lid: Лидер Гарантировано получит навык + на корабле может быть только 1 лидер, в случае если их возникает 2 то выбирается лучший
        :param bon: Добавляет характеристики к базовым 5 бонусам
        """

        self.name = generate_pirate_name()
        self.skill = None

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
            point -= 1
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





