import builtins
import types

import guess_the_word as gtw

class InputFeeder:
    
    def init(self, items): self._it = iter(items)

def __call__(self, prompt=""):
    return next(self._it)

def test_word_is_selected_from_predefined_list(monkeypatch):

    def choice_stub(seq):
    # record the exact object passed in
        called_with["arg"] = seq
    # return a valid element so the game can proceed
    return seq[0]

# Minimal inputs to finish the game quickly (guess all unique letters)
word0 = gtw.WORDS[0]
unique_letters = sorted(set(word0))

monkeypatch.setattr(gtw.random, "choice", choice_stub)
monkeypatch.setattr(builtins, "input", InputFeeder(unique_letters))

# Run one session; it will end by winning
gtw.play()

# Verify random.choice received the module's WORDS list
assert called_with["arg"] is gtw.WORDS
# And the chosen word is indeed in WORDS
assert choice_stub(gtw.WORDS) in gtw.WORDS

def test_guesses_processed_correctly(monkeypatch, capsys):

# Fix the secret word to 'loop' for determinism
    monkeypatch.setattr(gtw.random, "choice", lambda seq: "loop")

# Guesses: correct 'l', wrong 'x', correct 'o', correct 'p'
inputs = ["l", "x", "o", "p"]
monkeypatch.setattr(builtins, "input", InputFeeder(inputs))

gtw.play()
out = capsys.readouterr().out.lower()

# Check that correct and incorrect feedback appears
assert "good job! 'l' is in the word.".lower() in out
assert "sorry—'x' is not in the word.".lower() in out or "sorry-'x' is not in the word.".lower() in out
# The word should be guessed successfully
assert "congratulations! you guessed the word: loop" in out
