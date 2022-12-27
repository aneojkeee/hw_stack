from main import Stack

# Пример сбалансированных последовательностей скобок:
# (((([{}]))))
# [([])((([[[]]])))]{()}
# {{[()]}}
# Несбалансированные последовательности:
# }{}
# {{[(])]}}
# [[{())}]

def is_valid(lines):
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    open_par = Stack()

    if len(lines) % 2 > 0:
        return 'Несбалансированно'

    for i, fragment in enumerate(lines):
        if fragment in opening:
            open_par.push(fragment)
        elif fragment in closing:
            if open_par.is_empty():
                return 'Несбалансированно'
            elif opening.index(open_par.peek()) != closing.index(fragment):
                return 'Несбалансированно'
            else:
                open_par.pop()
                if open_par.is_empty() and i == len(lines)-1:
                    return 'Сбалансированно'


if __name__ == '__main__':
    print(is_valid(input('Введите строку')))