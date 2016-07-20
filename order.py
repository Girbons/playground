print "insert a word"
word = raw_input()
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

    if l == 25 or c == len(w):
        finish = True

if l == 25 and c < len(w):
    print("order false")

if c == len(word) and l <= 25:
    print("order true")
