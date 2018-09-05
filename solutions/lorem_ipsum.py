import string

with open("data/00-lorem-ipsum.txt") as f:
    d = {}
    for x in f.readlines():
        for s in string.punctuation:  # !"#$%&\'()*+,-./:;<=>?@[\\]^_‘{|}~
            x = x.replace(s, " ")
        for p in x.split():
            if p in d.keys():
                d[p] += 1
            else:
                d[p] = 1

    for key in sorted(d.keys()):
        if d[key] > 5:  # make the output a bit lighter...
            print("{}: {}".format(key, d[key]))
