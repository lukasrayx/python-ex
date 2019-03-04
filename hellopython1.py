def f(x,y):
    return x+y

from functools import reduce

r = reduce(f, [1,2,3,4,5,6,7,8,9,10])
print(r)

def normalize(name):
    name1 = name.lower()
    name2 = name1.title()
    return name2

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))

print(L2)

from functools import reduce
def prod1(x,y):
    return x*y

def prod(L):
    product = reduce(prod1,L)
    return product

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int(['1','2']))


from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))



def is_odd(n):
    return n % 2 == 1

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))



def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()


def is_palindrome(n):
    s_n = str(n)
    return s_n == s_n[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')




# 按名字排序
def by_name(t):
    return t[0].lower()

# 成绩从高到低排序
def by_score(t):
    return -t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)

L2 = sorted(L, key=by_score)
print(L2)


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
# 它们所引用的变量i已经变成了3，因此最终结果为9。

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())


def createCounter():
    f = 0
    print('闭包外--')

    def counter():
        print('闭包内--')
        nonlocal f
        f += 1
        return f
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')




