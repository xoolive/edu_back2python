import string
from collections import Counter

lw=[]
with open("data/00-lorem-ipsum.txt") as f:
    for l in f.readlines():
        for s in string.punctuation:  # !"#$%&\'()*+,-./:;<=>?@[\\]^_‘{|}~
            l = l.replace(s, " ")
        lw+=[w for w in l.split()]
        
c=Counter(lw)
print(c.most_common(5))