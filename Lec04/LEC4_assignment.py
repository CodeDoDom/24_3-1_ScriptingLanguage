def tmp_merge(*word):
    sen = ''
    cnt = len(word)     # 가변 인자의 개수

    for i in word:
        if cnt == 1:
            sen += 'and '
        sen += i
        cnt = cnt-1
        if cnt > 0:
            sen += ','

    print(f'문장: {sen}')
    print(f'타입: {type(sen)}')


tmp_merge('orange', 'apple', 'mango', 'banana', 'peanut')

#final = merge('orange', 'apple', 'mango', 'banana', 'peanut')
#final
#type(final)
