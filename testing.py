import random
import string


WORDS = [ "python", "variable", "function", "loop", "college", "community", "object", "integer", "boolean", "string", "module" ]

MAX_ATTEMPTS = 8

def displayprogress(word, guessed_letters):
    
return " ".join(ch if ch in guessed_letters else "" for ch in word)

def get_letter(already_tried):

while True:
    entry = nput("Enter a letter: ").strip().lower()
    if len(entry) != 1 or entry not in string.ascii_lowercase:
        print("Please type exactly one letter (a-z).")
        continue
    if entry in already_tried:
        print("You already tried that letter. Pick a new one.")
        continue
    return entry

def play(): """Run one game session."""
word = random.choice(WORDS)
guessed = set() # correct letters guessed so far
wrong = set() # incorrect letters guessed so far
attempts = MAX_ATTEMPTS
