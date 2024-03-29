def hide_vowel(w):
    h = ""
    for c in w:
        if c.lower() in 'aeiou':
            c = '*'
        h += c
    return h


def less_offensive(t, oword):
    for i in range(len(t)):
        l_oword = len(oword)
        word = t[i: i + l_oword]
        if l_oword == len(word) and word.lower() == oword.lower():
            new_word = hide_vowel(word)
            t = t[0:i] + new_word + t[i+l_oword:]
    return t


owords = input().split()
text = input()

for oword in owords:
    text = less_offensive(text, oword)

print(text)
