import string
import sys
import os
import random

class Histogram:
    def __init__(self, source_text, order=1):
        self.total_words = set()
        self.hist = self._generate_histogram(source_text)
        self.chain = self._build_markov_chain(source_text, order)
        self.order = order

    def _preprocess_text(self, source_text):
        # Read the source text file or use the contents directly if provided as a string
        if isinstance(source_text, str):
            if os.path.isfile(source_text):
                try:
                    with open(source_text, 'r') as file:
                        text = file.read()
                except FileNotFoundError:
                    print(f"Error: File '{source_text}' not found.")
                    sys.exit(1)
            else:
                text = source_text
        elif isinstance(source_text, list):
            # Join the list elements into a single string
            text = " ".join(source_text)
        else:
            # Invalid input type, raise an exception or handle it accordingly
            raise ValueError("Invalid source_text type. Expected string or list.")

        return text


    def _generate_histogram(self, source_text):
        # Split the text into words
        words = self._preprocess_text(source_text).split()
        self.total_words.update(words)

        # Create a dictionary to store word frequencies
        histogram = {}
        for word in words:
            histogram[word] = histogram.get(word, 0) + 1

        return histogram

    def _build_markov_chain(self, source_text, order):
        chain = {}
        words = self._preprocess_text(source_text).split()

        for i in range(len(words) - order):
            current_state = tuple(words[i:i+order])
            next_word = words[i + order]

            if current_state in chain:
                chain[current_state].append(next_word)
            else:
                chain[current_state] = [next_word]

        return chain

    def unique_words(self):
        # Count the number of unique words in the histogram
        return len(self.hist)

    def frequency(self, word):
        # Get the frequency of the given word from the histogram
        return self.hist.get(word, 0)

    def generate_random_word(self):
        # Set the keys and weights
        keys = list(self.hist.keys())
        weights = list(self.hist.values())

        # Grab a random key based on the frequency of occurrence
        word = random.choices(keys, weights=weights)[0]

        return word

    def get_total_unique_words(self):
        # Count the unique words from the histogram
        return self.unique_words()

    def get_total_words(self):
        # Return the total number of words
        return len(self.total_words)

    def get_frequency(self, word):
        # Return the frequency of a given word
        return self.frequency(word)

    def get_random_word(self):
        # Return a random word based on a weighted system
        return self.generate_random_word()
    
    def get_word_frequencies(self):
        # Generate a list of tuples containing unique words and their frequencies
        return list(self.hist.items())

    def generate_random_phrase(self, which):
        if which == "markov":
            random_words = []
            current_state = random.choice(list(self.chain.keys()))

            for _ in range(random.randint(1, 30)):
                random_words.append(current_state[-1])
                next_word_options = self.chain.get(current_state, [])
                if next_word_options:
                    next_word = random.choice(next_word_options)
                    current_state = tuple(list(current_state)[1:] + [next_word])
                else:
                    break

            phrase = " ".join(random_words)
            phrase = phrase.capitalize() + '.'
            phrase = self.apply_punctuation_changes(phrase)
            return phrase
        else:
            return "Did not receive a choice."

    def apply_punctuation_changes(self, phrase):
        # List of punctuation marks to consider
        punctuation_marks = string.punctuation

        # Iterate over the phrase and make necessary changes
        words = phrase.split()
        for i in range(len(words)):
            word = words[i]

            if '"' in word and "'" in word:
                # Remove both single quotes and double quotes
                word = word.replace("'", "").replace('"', "")
            elif "'" in word:
                # Remove single quotes
                word = word.replace("'", "")
            elif '"' in word:
                # Remove double quotes
                word = word.replace('"', "")

            words[i] = word

            if word == "i":
                words[i] = word.capitalize()

            if len(word) > 1 and word[-1] in punctuation_marks:
                # Separate the word from the trailing punctuation mark
                punctuation = word[-1]
                word = word[:-1]  # Remove the last character (punctuation mark) from the word

                # Apply grammar changes based on punctuation type
                if punctuation == '.' or punctuation == '!' or punctuation == '?':
                    # Capitalize the first letter of the next word
                    if i + 1 < len(words):
                        words[i + 1] = words[i + 1].capitalize()

                # Reassign the modified word with the punctuation mark to the list

                words[i] = word + punctuation


        return ' '.join(words)

    def get_random_phrase(self, which):
        return self.generate_random_phrase(which)



fish_file = "./data/fish.txt"
dracula_file = "./data/dracula.txt"

if __name__ == "__main__":
    hist = Histogram(dracula_file, order=2)
    print("\nThis is now the markov chain:\n")
    for _ in range(random.randint(1, 5)):
        print(hist.get_random_phrase("markov"))
