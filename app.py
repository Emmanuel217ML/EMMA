def get_input():
    while True:
        word = input(prompt).strip()
        if word:
            return word
        print("Oops! Please enter a valid word.")

def count_words():
    total = 0
    total += len(noun.split())
    total += len(verb.split())
    total += len(adjective.split())
    total += len(place.split())
    print(f"\nTotal words you entered: {total}")

# --- Input Section (Each with its own variable) ---
prompt = "Enter a noun: "
noun = get_input()

prompt = "Enter a verb: "
verb = get_input()

prompt = "Enter an adjective: "
adjective = get_input()

prompt = "Enter a place: "
place = get_input()

# --- Story Creation ---
story = f"\nOne day, a {adjective} {noun} decided to {verb} at the {place}."

# --- Output ---
print("\nYour Mad Libs story:")
print(story)

count_words()