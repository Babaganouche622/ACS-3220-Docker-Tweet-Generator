import random
import sys

arguments = sys.argv[1:]

# Shuffle the arguments
random.shuffle(arguments)

# Join the shuffled arguments with a comma and space
shuffled_arguments = " ".join(arguments)

if __name__ == '__main__':
    quote = shuffled_arguments
    print(quote)