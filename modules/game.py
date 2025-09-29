class Wordle:
    def __init__(self, word: str):
        assert len(word) == 5
        self.word = word.upper()
        self.guesses = []

    def guess(self, guess):
        assert len(guess) == 5
        guess = guess.upper()

        word = list(self.word)
        result = Wordle._score_guess(self.word, guess)

        self.guesses.append((guess, result))
        return result

    @staticmethod
    def _score_guess(secret: str, guess: str):
        """Return Wordle-style result list for guess against secret (0/1/2)."""
        secret = secret.upper()
        guess = guess.upper()
        s_list = list(secret)  # mutable copy to mark consumed letters
        result = [0] * 5

        # greens first
        for i in range(5):
            if guess[i] == s_list[i]:
                result[i] = 2
                s_list[i] = None

        # then yellows using remaining letters (consumes matches)
        for i in range(5):
            if result[i] == 0:
                try:
                    j = s_list.index(guess[i])  # find a remaining matching letter
                except ValueError:
                    continue
                result[i] = 1
                s_list[j] = None

        return result

    def is_possible(self, candidate):
        """Return True iff candidate word is consistent with all past guess results."""
        assert len(candidate) == 5
        candidate = candidate.upper()

        for past_guess, past_result in self.guesses:
            # simulate past_guess against candidate-as-secret
            simulated = self._score_guess(candidate, past_guess)
            if simulated != past_result:
                return False

        return True


if __name__ == "__main__":
    word = input("> ").strip()
    w = Wordle(word)
    while True:
        play = input("> ").strip().split()
        assert len(play) == 2
        guess = play[1]

        if play[0] == "guess":
            print("".join(str(x) for x in w.guess(guess)))
        elif play[0] == "check":
            print(w.is_possible(guess))
