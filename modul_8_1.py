'''Домашнее задание по теме Try and Except'''

def add_everything_up(a, b):
    try:
        c = a + b
        print('start try')
    except TypeError:
        print('start except')
        return (f'result add - {str(a) + str(b)}')
    else:
        print('a and are of the same type')
        return (f' result add- {c}')
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 125.626))
print(add_everything_up('qwe', 'rty'))
