import spacy
from collections import Counter

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Function to process a chunk of text and filter stop words
def process_chunk(text):
    filtered_words = []
    doc = nlp(text)
    for token in doc:
        if not token.is_stop and token.is_alpha:
            filtered_words.append(token.text.lower())  # Convert to lowercase for case-insensitive counting
    return filtered_words

# Function to count word frequencies
def count_word_frequencies(words):
    word_freq = Counter(words)
    return word_freq

# Open the text file and read it in chunks
with open('paragraphs.txt', 'r') as file:
    word_freq = Counter()
    chunk_size = 1000000  # Adjust the chunk size as needed
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        # Process the chunk
        filtered_words = process_chunk(chunk)
        # Count word frequencies
        word_freq.update(filtered_words)

# Print the most common words and their frequencies
print("Most common words and their frequencies:")
for word, freq in word_freq.most_common(10):  # Change 10 to the desired number of top words
    print(f"{word}: {freq}")
