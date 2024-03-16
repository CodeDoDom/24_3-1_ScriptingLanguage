def merge(*word):
    sen = ''
    cnt = len(word)     # 가변 인자의 개수

    for i in word:
        if cnt == 1:
            sen += 'and '
        sen += i
        cnt = cnt-1
        if cnt > 0:
            sen += ','

    return sen
    

final = merge('orange', 'apple', 'mango', 'banana', 'peanut')
print(final)
print(type(final))


# copilot
def c_merge(*args):
    # Join all input strings with commas
    result = ', '.join(args)

    # Insert 'and' before the last string
    last_comma_index = result.rfind(',')
    if last_comma_index != -1:
        result = result[:last_comma_index] + ' and' + result[last_comma_index + 1:]

    return result


# Example usage
final = c_merge('orange', 'apple', 'mango', 'banana', 'peanut')
print(final)  # Output: 'orange, apple, mango, banana, and peanut'
print(type(final))  # Output: <class 'str'>
