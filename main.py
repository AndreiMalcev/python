# НОМЕРОМ В СПИСКЕ ЛИТЕРАТУРЕ БУДЕМ СЧИТАТЬ ПОСЛЕДОВАТЕЛЬНОСТЬ ПОДРЯД ИДУЩИХ СИМВОЛОВ: /n + number + .
RESULT = ""


# возвращает True, если является номером, иначе False
def is_number_literature(line):
    if line[0] == '\n' and line[1:len(line) - 1].isdigit() and line[len(line) - 1] == '.':
        return True
    return False


# кладем в переменную RESULT отформатированный пункт литературы в виде: number. Literature/n
def put_in_result(number, str):
    global RESULT
    RESULT += '{0}.{1}\n'.format(number, str)

def editor(path):
    file = open(path, 'r')
    input_file = '\n'
    for line in file:
        input_file += line
    prev_index = 1
    next_index = -1
    index = 1
    first = True
    for i in range(3, len(input_file)):
        if is_number_literature(input_file[i: i + len(str(index + 1)) + 2]):
            if first:
                next_index = i + 1
                first = False
            else:
                prev_index = next_index
                next_index = i + 1
            put_in_result(index, input_file[prev_index + len(str(index)) + 1: next_index].replace('\n', ' '))
            index += 1
    put_in_result(index, input_file[next_index + len(str(index)) + 1: len(input_file)].replace('\n', ' '))
    print(RESULT)
    file.close()

editor('file/references6.txt')
RESULT = ""
editor('file/references7.txt')