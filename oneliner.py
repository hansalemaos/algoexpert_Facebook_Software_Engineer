import itertools
tele=3662277
words=['bar', 'foo', 'car', 'cat','foobar','cap','emo']
phonedict={'a':2, 'b':2, 'c':2,   'd':3, 'e':3, 'f':3,   'g':4, 'h':4, 'i':4,   'j':5, 'k':5, 'l':5,   'm':6, 'n':6, 'o':6,   'p':7, 'q':7, 'r':7, 's':7,   't':8, 'u':8, 'v':8,   'w':9, 'x':9, 'y':9, 'z':9, }
result = ["".join(list(i[0])) for i in zip([tuple([str(y) for y in x]) for x in words],[tuple([str(phonedict.get(y)) for y in x]) for x in words]) if i[1] in tuple(set.union(*[set(q) for q in [[pp for pp in p if pp in  [tuple([str(phonedict.get(y)) for y in x]) for x in words]] for p in [[k for k in wordsasnumberx] for wordsasnumberx in tuple( (((itertools.combinations_with_replacement(list(str(tele)),r=x)))) for x in range(0,len(str(tele))))]] if q])) ]
print(result )
# ['bar', 'foo', 'car', 'foobar', 'cap', 'emo']
