def detect_anagrams(word, pos_anagrams):

    w = word.lower()
    ref = sorted(w)

    anagrams = []
    for p in pos_anagrams:
        
        if p.lower() == w:
            continue

        test = sorted(p.lower())

        if test == ref:
            anagrams.append(p)

    return anagrams
