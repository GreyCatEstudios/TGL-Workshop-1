import string


def count_words(file_name):
    with open(file_name, 'r') as file:
        text = file.read()

    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Convert the text to lower case and split it into words
    words = text.lower().split()

    # Count the occurrence of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Print the words and their counts
    for word, count in word_counts.items():
        print(f"{word}: {count}")


# Use the function
count_words("your_file.txt")
