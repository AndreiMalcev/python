NAME = 'бабушка'
ACTION = 'купим'
OBJECT = 'телевизор'
ANIMALS = [['курочку', 'Курочка по зёрнышку кудах-тах-тах'],
           ['уточку', 'Уточка та-ти-та-та'],
           ['индюшонка', 'Индюшонок фалды-балды'],
           ['кисоньку', 'А кисуня мяу-мяу'],
           ['собачонку', 'Собачонка гав-гав'],
           ['коровёнку', 'Коровёнка муки-муки'],
           ['поросёнка', 'Поросёнок хрюки-хрюки']]
BASE_LINE = '{0}, {1}, {2} '.format(NAME.title(), NAME, ACTION)
END_LINE = '{0} надо, надо, ведь у нас такое стадо!'.format(OBJECT.title())
NEXT_LINE = '\n'
EXCLAMATION_MARK = '!'
COMMA = ','
DOT = '.'
REPEAT = 2


def two_lines(s):
    return NEXT_LINE.join([BASE_LINE + s + EXCLAMATION_MARK] * REPEAT)


used_lines = []
for (animal, line) in ANIMALS:
    print(two_lines(animal))
    used_lines.append(line)
    for i, string in enumerate(used_lines[::-1]):
        print(string + (DOT + NEXT_LINE if i == len(used_lines) - 1 else COMMA))
print(two_lines(OBJECT) + NEXT_LINE + END_LINE)
