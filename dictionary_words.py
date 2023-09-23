import random
import sys

def generate_random_quote(random_number):
    with open("/usr/share/dict/words", "r") as f:
        words = f.readlines()
    
    random_words = []
    for _ in range(random_number):
        random_words.append(random.choice(words).strip())
    random_quote = " ".join(random_words)
    random_quote = random_quote.capitalize() + "."
    
    return random_quote

if __name__ == '__main__':
    random_number = int(sys.argv[1])
    quote = generate_random_quote(random_number)
    print("Random quote:", quote)