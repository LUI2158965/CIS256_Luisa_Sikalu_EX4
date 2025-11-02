import random
import string


WORDS = [ "python", "variable", "function", "loop", "college", "community", "object", "integer", "boolean", "string", "module" ]

MAX_ATTEMPTS = 8

def display_progress(word, guessed_letters):
    
    return " ".join(ch if ch in guessed_letters else "" for ch in word)

def get_letter(already_tried):

    while True:
        entry = input("Enter a letter: ").strip().lower()
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

   
    
print("Welcome to Guess the Word!")
print(f"You have {8} attempts to guess the word.")

while attempts > 0:
    print("\nWord:    ", display_progress(word, guessed))
    print("wrong:    ", " ".join(sorted(wrong)) if wrong else "(none)")
    print(f"Attempts: {8}")

    letter = get_letter(guessed | wrong)

    if letter in word:
        guessed.add(letter)
        print(f"Good job! '{letter}' is in the word.")
        # Check if all unique letters have been guessed
        if all(ch in guessed for ch in set(word)):
            print("\nCongratulations! You guessed the word:", word)
            
    else:
        wrong.add(letter)
        attempts -= 1
        print(f"Sorry—'{letter}' is not in the word.")

print("\nOut of attempts. The word was:", word)
