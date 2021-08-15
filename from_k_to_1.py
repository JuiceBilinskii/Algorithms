n = int(input())

length = {
    1: [0, 0]
}
current_num = 1
while current_num != n:
    for fun in [lambda a: a + 1, lambda a: a * 2, lambda a: a * 3]:
        new_num = fun(current_num)
        if not length.get(new_num, None):
            length[new_num] = [length[current_num][0] + 1, current_num]
        else:
            length[new_num] = [length[current_num][0] + 1, current_num] if length[current_num][0] + 1 < length[new_num][0] else length[new_num]
    current_num += 1


def list_generator():
    num = yield
    leng = yield
    while num != 0:
        yield num
        num = leng[num][1]


l_gen = list_generator()
l_gen.send(None)
l_gen.send(n)
l_gen.send(length)

sequence = ' '.join([str(i) for i in l_gen][::-1] + [str(n)])
print(length[n][0])
print(sequence)
