# version #1
def merge(*fruits):
    res = ''
    for fruit in fruits[:-1]:
        res += f'{fruit}, '
    res += ('and ' if res else '') + fruits[-1]
    return res


# print(merge('apple'), '/    답: apple')
# print(merge('apple', 'banana'), '/    답: apple, and banana')
# print(merge('apple', 'banana', 'mange', 'cherry'), '/    답: apple, banana, mango, and cherry')

assert(merge('apple') == 'apple')
assert(merge('apple', 'banana') == 'apple, and banana')
assert(merge('apple', 'banana', 'mango', 'cherry') == 'apple, banana, mango, and cherry')
