import string
from collections import defaultdict

with open("data/00-lorem-ipsum.txt") as f:
    d = defaultdict(int)
    for x in f.readlines():
        for s in string.punctuation:  # !"#$%&\'()*+,-./:;<=>?@[\\]^_‘{|}~
            x = x.replace(s, " ")
        for p in x.split():
            d[p] += 1

    for key in sorted(d.keys()):
        if d[key] > 5:  # make the output a bit lighter...
            print(f"{key}: {d[key]}")
