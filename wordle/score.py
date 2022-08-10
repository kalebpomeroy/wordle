def letter_scores(words):
    """
        Given a list of words, score each letter, for each postion. The sixth
        position is the total sum of the letter, regardless of position.
        [
            { "a": 5, "b": 7, "c": 2, "d": 1, "e": 8 ... }
            { "a": 4, "b": 8, "c": 9, "d": 5, "e": 7 ... }
            { "a": 5, "b": 9, "c": 4, "d": 9, "e": 9 ... }
            { "a": 3, "b": 6, "c": 2, "d": 8, "e": 3 ... }
            { "a": 1, "b": 2, "c": 1, "d": 4, "e": 12 ... }
            { "a": 18, "b": 32, "c": 18, "d": 27, "e": 39 ... }
        ]
    """

    letters = [{},{},{},{},{},{}]

    for word in words:
        i = 0
        for i, letter in enumerate(word):
            letters[i][letter] = letters[i].get(letter, 0) + 1
            letters[5][letter] = letters[5].get(letter, 0) + 1
    return letters


def word_scores(words, skip_repeated_chars=True, use_positional=True):
    """
        Given a list of words, figure out which has the higest score.

        skip_repeated_chars - Skip words with duplicate characters. The highest
                              total scoring word is `eerie` but that doesn't
                              make it a great starting guess
        use_positional      - will use the positional score by default. If set
                              to false, it will use the total positional score.
                              `alert` has a higher total score than `slate`.
                              However, `slate` has a higher positional score due
                              to the ending `e` being a highly common ending
    """
    l_scores = letter_scores(words)
    scores = {}
    for word in words:
        if skip_repeated_chars and has_repeated_chars(word):
            continue

        score = 0
        for i, letter in enumerate(word):
            key = i if use_positional else 5
            score += l_scores[key][letter]

        scores[word] = score
    return scores


def get_highest_score_word(word_list, **kwargs):
    w_scores = word_scores(word_list, **kwargs)
    return max(w_scores, key=w_scores.get)


def has_repeated_chars(s):
    for i in xrange(len(s)):
        if i != s.rfind(s[i]):
            return True
    return False
