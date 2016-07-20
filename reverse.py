print "insert a word"
word = raw_input()
w = list(word)
finish = False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l = 25
c = 0

while finish is False:

    if w[c] == alphabet[l]:
        c += 1
        l -= 1
    else:
        l -= 1

    if l == 0:
        if w[c] == alphabet[l]:
            c += 1

    if c == len(w):
        finish = True


if l == 0 and c < len(w):
    print "not reverse"

if c == len(w) and l >= 0:
    print "reverse"