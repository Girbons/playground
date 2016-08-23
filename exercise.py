def count_letters(w):
    l = list(w)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    i = 0
    c = 0
    t1 = 0
    t2 = 0
    t3 = 0

    while c < len(l):
        if c < len(l) and i > 25:
            i = 0

        if alphabet[i] == l[c]:
            t1 += 1
            c += 1

            if t1 > t2:
                t2 = t1
                t3 = alphabet[i]
        else:
            i += 1
            t1 = 0

    if len(l) > 1 and t2 == 1:
        t3 = 0

    return t3


def test():
    assert (count_letters('aabc') == 'a')
    assert (count_letters('aaabbbbaacc') == 'b')
    assert (count_letters('aaabbaacccc') == 'c')
    assert (count_letters('z') == 'z')
    assert (count_letters('abcd') == 0)
    print('Letters counted successfully')

test()
