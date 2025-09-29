import math
import wordfreq
from modules import game

STARTERS = "roate", "soare", "stare"

class Analyzer:
    def __init__(self, word: str, words_list: list, normalize_frequency: bool = True):
        self.word = word
        self.words_list = words_list.copy()
        self.normalize_frequency = normalize_frequency

    def analyze_guesses(self, guesses: list):
        """
        get bits of information gained from guesses
        """
        wdl = game.Wordle(self.word)
        bits = []
        wordlist = self.words_list.copy()
        for guess in guesses:
            p = len(wordlist)
            wdl.guess(guess)
            for word in tuple(wordlist):
                if not wdl.is_possible(word):
                    wordlist.remove(word)
            pdash = len(wordlist)
            bits.append((math.log2(p/pdash), p, pdash))
        
        return bits
        

    def get_best_guesses(self, past_guesses: list):
        """
        get best guesses in current position
        """
        if not past_guesses:
            return list(STARTERS)

        wordlist = self.words_list.copy()
        wdl = game.Wordle(self.word)
        for guess in past_guesses:
            wdl.guess(guess)
        for word in tuple(wordlist):
            if not wdl.is_possible(word):
                wordlist.remove(word)

        data = []
        i = 1
        for guess_word in wordlist:
            s = 0

            # calculate best guess by bits gained if less than 20 possibilities
            if len(wordlist) <= 20:
                _p = wordlist.copy()
                j = 1
                for word in wordlist:
                    a = (i / len(wordlist)) * 100
                    b = (j / len(_p)) * 100
                    print(f"{a:6.2f}% {b:6.2f}%   ", end="\r")
                    _wdl = game.Wordle(word)
                    _wdl.guess(guess_word)
                    _pdash = []
                    for _word in _p:
                        if _wdl.is_possible(_word):
                            _pdash.append(_word)
                    if _pdash:
                        score = math.log2(len(_p)/len(_pdash))
                        s += score
                    j += 1

            # use "score" method otherwise
            else:
                for word in wordlist:
                    _wdl = game.Wordle(word)
                    result = _wdl.guess(guess_word)
                    score = sum(result)
                    s += score

            data.append((guess_word, s))
            i += 1

        data.sort(key=lambda x: (-x[1], x[0]))

        # at this stage, data[0][0] is the best guess

        if self.normalize_frequency:
            # keep only first 10% of guesses (at least 10)
            n = max(10, int(0.1 * len(data)))
            data = data[:n]

            # sort this data by popularity
            data.sort(key=lambda x: (-wordfreq.word_frequency(x[0], "en"), x[0]))

        return [guess[0] for guess in data][:10]