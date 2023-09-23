import string
import sys
import os
import random

total_words = ""

def histogram(source_text):
    global total_words
    # Read the source text file or use the contents directly if provided as a string
    if isinstance(source_text, str) and os.path.isfile(source_text):
        with open(source_text, 'r') as file:
            text = file.read()
    else:
        text = source_text

    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split the text into words
    words = text.split()
    total_words = words
    # Create a dictionary to store word frequencies
    histogram = {}
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1

    return histogram

def unique_words(histogram):
    # Count the number of unique words in the histogram
    return len(histogram)

def frequency(word, histogram):
    # Get the frequency of the given word from the histogram
    return histogram.get(word, 0)

def generate_random_word(word_list):
    # Set the keys and weights
    keys = list(word_list.keys())
    weights = list(word_list.values())

    # Grab a random key based on the frequency of occurence
    word = random.choices(keys, weights=weights)[0]
    
    return word


# Example usage
source_text = "one fish two fish red fish blue fish"

dracula_file = "./data/dracula.txt"

# Which file or sample text are be using?
hist = histogram(dracula_file)
# hist = histogram(source_text)

# Count the unique words from the histogram
unique_count = unique_words(hist)

# Count the frequency of a given word
mystery_count = frequency(sys.argv[1], hist)

# Grab a random word based off a weighted system
random_word = generate_random_word(hist)

print("Total unique words:", unique_count)
print("Total words:", len(total_words))
print(f"Frequency of '{sys.argv[1]}':", mystery_count)
print(f"Random word: {random_word}")
