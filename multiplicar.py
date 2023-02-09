import copy


def multiplicar(*args):
    total = 1
    for item in args:
        total *= item
    return total

print(multiplicar(6,5,4,3,2,1))


def pair(x):
    if x % 2 == 0:
        return f'{x} é par! '
    return f'{x} é ímpar! '

print(pair(13))


def double(x):
    return f'{x * 2}  {x*3}  {x*4}'

print(double(3))


d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [1,2,3],
}

d2 = d1.copy()
d2['c2'] = 200
d3 = copy.deepcopy(d2)
d2['l1'][2] = 300
d3['l1'][1] = 2500

print(d1)
print(d2)
print(d3)
