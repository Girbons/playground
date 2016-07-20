def simple_alphabet_order(word):
    w = list(word)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    finish = False

    c = 0
    l = 0

    while finish is False:
        if w[c] == alphabet[l]:
            c += 1
        else:
            l += 1
        if l == 25:
            if w[c] == alphabet[l]:
                c += 1
        if l == 25 or c == len(w):
            finish = True

    if l == 25 and c < len(w):
        return False

    if c == len(word) and l <= 25:
        return True


def test():
    assert simple_alphabet_order('almost') == True
    assert simple_alphabet_order('cereal') == False
    assert simple_alphabet_order('billowy') == True
    assert simple_alphabet_order('biopsy') == True
    assert simple_alphabet_order('chinos') == True
    assert simple_alphabet_order('defaced') == False
    assert simple_alphabet_order('chintz') == True
    assert simple_alphabet_order('bijoux') == True
    assert simple_alphabet_order('abhors') == True
    assert simple_alphabet_order('fiddle') == False
    assert simple_alphabet_order('begins') == True
    assert simple_alphabet_order('chimps') == True
    # bonus tests
    # assert simple_alphabet_order('sponged') == True
    # assert simple_alphabet_order('wronged') == True

test()